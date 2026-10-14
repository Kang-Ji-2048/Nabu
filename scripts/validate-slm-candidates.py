"""Package reviewed-by-assistant risk proposals without training or GPU inference.

Only explicit train/validation historical drafts are read. Passing mechanical
validation does not establish semantic support or human approval.
"""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.risk.contracts import Detection
from nabu.risk.runner import validate_detection


def identity_sha256(value):
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def read_sources(train_drafts, validation_drafts):
    """Fail closed on test sources, wrong partitions, or duplicate identities."""
    sources, seen = [], set()
    paths = [Path(train_drafts).resolve(), Path(validation_drafts).resolve()]
    if paths[0] == paths[1]:
        raise ValueError("Train and validation must be distinct explicit source files")
    for split, path in zip(("train", "validation"), paths):
        if "test" in path.stem.lower().split("-"):
            raise ValueError("Held-out test source files are forbidden")
        content = path.read_bytes()
        file_sha = hashlib.sha256(content).hexdigest()
        for number, line in enumerate(content.decode("utf-8").splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict) or row.get("split") != split:
                raise ValueError(f"{path}:{number}: only {split} source rows are allowed; held-out test rows are forbidden")
            if not isinstance(row.get("id"), str) or not row["id"]:
                raise ValueError(f"{path}:{number}: source row requires a nonempty string ID")
            if row["id"] in seen:
                raise ValueError(f"Duplicate source ID: {row['id']}")
            for required in ("as_of", "input", "evidence_fingerprint"):
                if required not in row:
                    raise ValueError(f"{path}:{number}: source row lacks {required}")
            if not isinstance(row["input"], dict):
                raise ValueError(f"{path}:{number}: source input must be an object")
            seen.add(row["id"])
            sources.append({"row": row, "path": str(path), "line": number,
                            "file_sha256": file_sha})
    return sources


def read_proposals(path, known_ids):
    """Record every malformed/unknown proposal; never infer an empty target."""
    content = Path(path).read_bytes()
    proposals, errors = {}, []
    for number, line in enumerate(content.decode("utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            proposal = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append({"status": "malformed_proposal", "line": number,
                           "response": line, "errors": [str(exc)]})
            continue
        if not isinstance(proposal, dict) or not isinstance(proposal.get("id"), str):
            errors.append({"status": "malformed_proposal", "line": number,
                           "proposal": proposal, "errors": ["Proposal requires a string ID"]})
            continue
        if proposal["id"] not in known_ids:
            errors.append({"status": "unknown_proposal_id", "line": number,
                           "proposal": proposal, "id": proposal["id"],
                           "errors": ["ID does not belong to the supplied train/validation drafts"]})
            continue
        proposals.setdefault(proposal["id"], []).append({**proposal, "line": number})
    return proposals, errors, hashlib.sha256(content).hexdigest()


def proposal_errors(proposal, payload):
    if "target" not in proposal:
        return ["Proposal is missing target"], None
    questions = proposal.get("labelling_questions", [])
    if not isinstance(questions, list) or any(not isinstance(q, str) or not q.strip() for q in questions):
        return ["labelling_questions must be a list of nonempty strings"], None
    try:
        target = Detection.model_validate(proposal["target"]).model_dump()
        result = validate_detection(target, payload)
    except (ValueError, TypeError, KeyError) as exc:
        return [f"{type(exc).__name__}: {exc}"], None
    if result["rejected"]:
        return result["rejected"], None
    seen = set()
    for risk in target["risks"]:
        key = (" ".join(risk["claim"].casefold().split()),
               tuple(sorted(risk["target_item_ids"])))
        if key in seen:
            return ["Duplicate risk claims for the same plan targets"], None
        seen.add(key)
    return [], target


def json_block(value):
    return ["```json", json.dumps(value, ensure_ascii=False, indent=2), "```", ""]


def review_document(entries, proposal_events):
    lines = ["# Nabu candidate supervised risk labels", "",
             "These assistant-generated targets are unreviewed. Mechanical validation checks the Detection schema, allowed risk types, plan targets and exact historical citations. It does not verify causal support, usefulness, severity or completeness. No human approval or reviewer is claimed. Held-out test examples are excluded.", ""]
    valid = [entry for entry in entries if entry["event"]["status"] == "generated_unreviewed"]
    positive = sum(bool(entry["event"]["target"]["risks"]) for entry in valid)
    lines.extend([f"Examples: {len(entries)}. Valid risk examples: {positive}; valid evidence-insufficient/no-risk examples: {len(valid) - positive}; failed or missing examples: {len(entries) - len(valid)}.", "",
                  "An empty risk list means that this supplied evidence did not support a risk; it does not certify a safe plan.", "",
                  "## Case index", "", "| Case | Split | Risk count | Status |", "| --- | --- | ---: | --- |"])
    for entry in entries:
        row, event = entry["source"], entry["event"]
        risk_count = event.get("risk_count", "—")
        anchor = f"{row['id']}-{row['split']}".lower()
        lines.append(f"| [{row['id']}](#{anchor}) | {row['split']} | {risk_count} | {event['status']} |")
    lines.append("")
    for entry in entries:
        row, event = entry["source"], entry["event"]
        payload, plan = row["input"], row["input"]["plan"]
        lines.extend([f"## {row['id']} ({row['split']})", "",
                      f"Historical cutoff: {row['as_of']}", "",
                      f"Status: **{event['status']}**", "",
                      f"Evidence fingerprint: `{row['evidence_fingerprint']}`", "",
                      f"Source input identity SHA-256: `{identity_sha256(payload)}`", "",
                      "### Supplied historical plan", ""])
        for item in [plan["root"], *plan.get("members", [])]:
            lines.extend([f"- **{item.get('source_key', item['id'])}** (`{item['id']}`)",
                          f"  - Title: {json.dumps(item['fields'].get('title'), ensure_ascii=False)}",
                          f"  - Description: {json.dumps(item['fields'].get('description'), ensure_ascii=False)}",
                          f"  - Unknown fields: {json.dumps(item.get('unknown_fields', []), ensure_ascii=False)}",
                          f"  - Truncated fields: {json.dumps(item.get('truncated_fields', []), ensure_ascii=False)}"])
        lines.extend(["", "### Proposed target", ""])
        if "target" in event:
            lines.extend(json_block(event["target"]))
        elif "proposals" in event:
            lines.extend(json_block(event["proposals"]))
        else:
            lines.extend(["No proposal was supplied. No no-risk target was inferred.", ""])
        if event.get("errors"):
            lines.extend(["Validation failures:", "", *json_block(event["errors"])])
        target = event.get("target")
        if isinstance(target, dict) and isinstance(target.get("risks"), list):
            evidence = {i["id"]: i for i in payload["prior_work"]}
            for risk in target["risks"]:
                if not isinstance(risk, dict):
                    continue
                lines.extend([f"#### Evidence for {risk.get('id', 'unnamed risk')}", ""])
                citations = risk.get("citations", [])
                for citation in citations if isinstance(citations, list) else []:
                    if not isinstance(citation, dict):
                        continue
                    item_id = citation.get("item_id")
                    item = evidence.get(item_id) if isinstance(item_id, str) else None
                    key = item.get("source_key", item["id"]) if item else "UNKNOWN TICKET"
                    lines.append(f"- {key} / `{citation.get('item_id')}` / {citation.get('field')}: {json.dumps(citation.get('quote'), ensure_ascii=False)}")
                lines.append("")
        lines.extend(["### Supplied prior evidence for support and counterexample review", ""])
        for item in payload["prior_work"]:
            lines.extend([f"- **{item.get('source_key', item['id'])}** (`{item['id']}`), created {item.get('created_at')}",
                          f"  - Title: {json.dumps(item['fields'].get('title'), ensure_ascii=False)}",
                          f"  - Description: {json.dumps(item['fields'].get('description'), ensure_ascii=False)}",
                          f"  - Unknown fields: {json.dumps(item.get('unknown_fields', []), ensure_ascii=False)}",
                          f"  - Truncated fields: {json.dumps(item.get('truncated_fields', []), ensure_ascii=False)}"])
        lines.extend(["", "### Unresolved labelling questions", ""])
        questions = entry.get("labelling_questions", [])
        if questions:
            lines.extend(f"- {q}" for q in questions)
        else:
            lines.extend(["- Does the proposed target correctly distinguish support from similarity, dependencies and incomplete scope?",
                          "- Does any supplied evidence or explicit plan work contradict the target?",
                          "- Are the limitations sufficiently specific to this historical example?"])
        lines.append("")
    if proposal_events:
        lines.extend(["## Unmatched or malformed proposal failures", "", *json_block(proposal_events)])
    return "\n".join(lines) + "\n"


def package_candidates(train_drafts, validation_drafts, proposals_path, output):
    output = Path(output).resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError("Output directory must be empty; existing candidates/events must not be overwritten")
    sources = read_sources(train_drafts, validation_drafts)
    known_ids = {source["row"]["id"] for source in sources}
    proposals, proposal_events, proposals_sha = read_proposals(proposals_path, known_ids)
    generated_at = datetime.now(timezone.utc).isoformat()
    candidates, events, entries = [], list(proposal_events), []
    counts = {split: {"total_examples": 0, "risk_examples": 0, "no_risk_examples": 0,
                      "failed_examples": 0, "missing_examples": 0, "proposed_risks": 0}
              for split in ("train", "validation")}
    for source in sources:
        row = source["row"]
        tally = counts[row["split"]]
        tally["total_examples"] += 1
        items = proposals.get(row["id"], [])
        event = {"id": row["id"], "split": row["split"], "as_of": row["as_of"],
                 "evidence_fingerprint": row["evidence_fingerprint"],
                 "source_input_sha256": identity_sha256(row["input"]),
                 "source_row_sha256": identity_sha256(row), "generated_at": generated_at}
        questions = []
        if not items:
            event.update(status="missing_proposal", errors=["No proposed target was supplied"])
            tally["missing_examples"] += 1
        elif len(items) != 1:
            event.update(status="failed", proposals=items,
                         errors=["Duplicate proposals for the same example; none selected"])
            tally["failed_examples"] += 1
        else:
            proposal = items[0]
            errors, target = proposal_errors(proposal, row["input"])
            event.update(target=proposal.get("target"), proposal_line=proposal["line"])
            supplied_questions = proposal.get("labelling_questions", [])
            questions = supplied_questions if isinstance(supplied_questions, list) and all(isinstance(q, str) for q in supplied_questions) else []
            if errors:
                event.update(status="failed", errors=errors)
                tally["failed_examples"] += 1
            else:
                provenance = {"kind": "assistant_generated", "generator": "Codex",
                              "method": "supplied_historical_evidence_review", "human_approved": False,
                              "generated_at": generated_at, "source_draft_path": source["path"],
                              "source_draft_line": source["line"], "source_draft_sha256": source["file_sha256"],
                              "proposal_file_sha256": proposals_sha}
                labelled = {**deepcopy(row), "target": target, "review_status": "generated_unreviewed",
                            "label_source": provenance, "label_validation": "schema_and_exact_citations_only",
                            "source_input_sha256": identity_sha256(row["input"]),
                            "source_row_sha256": identity_sha256(row), "labelling_questions": questions}
                candidates.append(labelled)
                event.update(status="generated_unreviewed", target=target, risk_count=len(target["risks"]))
                tally["risk_examples" if target["risks"] else "no_risk_examples"] += 1
                tally["proposed_risks"] += len(target["risks"])
        events.append(event)
        entries.append({"source": row, "event": event, "labelling_questions": questions})
    total = {name: sum(tally[name] for tally in counts.values()) for name in counts["train"]}
    summary = {"status": "completed_with_failures" if total["failed_examples"] or total["missing_examples"] or proposal_events else "completed",
               "generated_at": generated_at, "review_status": "generated_unreviewed", "human_approved": False,
               "by_split": counts, "totals": total, "proposal_input_errors": len(proposal_events),
               "candidate_path": str(output / "generated-labels.jsonl"),
               "events_path": str(output / "label-events.jsonl"), "review_path": str(output / "review.md"),
               "summary_path": str(output / "summary.json"),
               "limitations": ["Mechanical validation does not establish semantic risk support or human approval.",
                               "Empty-risk targets mean insufficient supported risks in supplied text, not verified safety.",
                               "No test examples, GPU inference or training were used by this packaging tool."]}
    # Render every artifact before publishing. A malformed failed target or an
    # I/O failure must not leave apparently complete labels without their audit.
    rendered = {}
    for filename, rows in (("generated-labels.jsonl", candidates), ("label-events.jsonl", events)):
        rendered[filename] = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    rendered["review.md"] = review_document(entries, proposal_events)
    rendered["summary.json"] = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}-staging-", dir=output.parent))
    try:
        for filename, content in rendered.items():
            (staging / filename).write_text(content, encoding="utf-8")
        if output.exists() and (not output.is_dir() or any(output.iterdir())):
            raise ValueError("Output directory must be empty; existing candidates/events must not be overwritten")
        # Same-parent staging ensures rename publishes all four files together.
        # Replacing a nonempty directory is rejected by the OS even if another
        # writer races the final guard above.
        os.replace(staging, output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-drafts", type=Path, required=True)
    parser.add_argument("--validation-drafts", type=Path, required=True)
    parser.add_argument("--proposals", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    summary = package_candidates(args.train_drafts, args.validation_drafts, args.proposals, args.output)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if summary["status"] == "completed_with_failures" else 0


if __name__ == "__main__":
    raise SystemExit(main())
