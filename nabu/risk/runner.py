"""Resumable SLM-to-Claude assessment with frozen evidence and exact citations."""
import hashlib
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3

from ..agents.evidence import freeze_evidence, validate_findings
from ..classification import classify
from ..pipeline import timestamp
from ..text import text_of, tokens
from .contracts import Detection, ModelManifest, Presentation
from .models import ClaudeReporter, LocalSLM, OfflineDetector, OfflineReporter

VERSION = "nabu-assess-v1"


def read_manifest(path, cutoff):
    manifest = ModelManifest.model_validate_json(path.read_text(encoding="utf-8"))
    if not manifest.trained:
        raise ValueError("SLM training is incomplete; supply a trained model manifest or use --offline")
    trained_through = timestamp(manifest.trained_through, mandatory=True)
    if trained_through > cutoff:
        raise ValueError("SLM training cutoff is later than the review cutoff; historical evaluation would leak outcomes")
    return {**manifest.model_dump(), "trained_through": trained_through}


def compact(item):
    item = {**item, "fields": dict(item["fields"]),
            "truncated_fields": list(item.get("truncated_fields", []))}
    for name, limit in (("title", 200), ("description", 1200)):
        value = item["fields"][name]
        if isinstance(value, str) and len(value) > limit:
            item["fields"][name] = value[:limit]
            if name not in item["truncated_fields"]:
                item["truncated_fields"].append(name)
    # Recompute from cutoff-bound fields, never load latest snapshot categories.
    item["work_category"] = classify(text_of(item))
    return item


def detector_input(frozen, risk_types, evidence_limit):
    plan = frozen["plan"]
    members = plan["members"][:20]
    visible_plan = {**plan, "root": compact(plan["root"]), "members": [compact(i) for i in members]}
    words = tokens(" ".join(text_of(i) for i in [visible_plan["root"], *visible_plan["members"]]))
    ranked = sorted(frozen["corpus"].values(),
                    key=lambda item: (-len(words & tokens(text_of(item))), item["source_key"]))
    # No overlap means no lexical support; do not pad with arbitrary examples.
    selected = [compact(item) for item in ranked if words & tokens(text_of(item))][:evidence_limit]
    return {"plan": visible_plan, "prior_work": selected, "allowed_risk_types": risk_types,
            "coverage": {"retrieval": "lexical_overlap", "eligible_prior_items": len(ranked),
                         "supplied_prior_items": len(selected), "omitted_plan_members": len(plan["members"]) - len(members),
                         "warning": "Bounded lexical sample; scope, text and history may be incomplete. Work topics are rule labels, not learned risks."}}


def validate_detection(raw, payload):
    detection = Detection.model_validate(raw).model_dump()
    evidence = {item["id"]: item for item in payload["prior_work"]}
    state = {"plan": payload["plan"], "evidence": evidence}
    supported, errors = validate_findings(detection["risks"], state)
    valid = []
    for risk in supported:
        if risk["risk_type"] not in payload["allowed_risk_types"]:
            errors.append({"finding_id": risk["id"], "reasons": ["Risk type is not allowed by the trained model manifest"]})
        else:
            valid.append(risk)
    return {"risks": valid, "rejected": errors, "limitations": detection["limitations"]}


def validate_presentation(raw, risks):
    presentation = Presentation.model_validate(raw).model_dump()
    expected = {risk["id"] for risk in risks}
    actual = [section["risk_id"] for section in presentation["sections"]]
    if set(actual) != expected or len(actual) != len(expected):
        raise ValueError("Claude must present each detected risk exactly once, without adding risks")
    return presentation


def markdown(report):
    lines = ["# Nabu delivery risk review", "", f"Plan: {report['epic']} · Cutoff: {report['as_of']}", "",
             "Potential risks are suggestions for investigation, not validated predictions.", ""]
    if not report["analysis_performed"]:
        lines.extend(["**Offline wiring test: no AI analysis was performed.**", ""])
    if not report["risks"]:
        lines.extend(["No supported risks were returned. This does not establish that the plan is safe.", ""])
    sections = {section["risk_id"]: section for section in report["presentation"]["sections"]}
    for risk in report["risks"]:
        section = sections[risk["id"]]
        lines.extend([f"## {section['title']}", "", f"Severity: {risk['severity']} · Type: {risk['risk_type']}", "",
                      section["explanation"], "", f"**Next action:** {section['recommended_action']}", "",
                      "Supporting historical evidence:", ""])
        for citation in risk["citations"]:
            key = report["evidence_keys"][citation["item_id"]]
            # JSON encoding makes multiline excerpts explicit without breaking list formatting.
            lines.append(f"- {key} ({citation['field']}): {json.dumps(citation['quote'], ensure_ascii=False)}")
        lines.append("")
    lines.extend(["## Limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    return "\n".join(lines) + "\n"


def run_assessment(database, epic, cutoff, run_dir, *, offline=None, manifest_path=None,
                   slm_endpoint=None, claude_model=None, resume=False, pause_after_prepare=False,
                   evidence_limit=None, detector=None, reporter=None):
    run_dir = Path(run_dir).resolve()
    checkpoint = run_dir / "assessment.sqlite"
    if resume:
        if not checkpoint.exists():
            raise ValueError("No saved assessment exists")
        with closing(sqlite3.connect(checkpoint)) as connection:
            row = connection.execute("SELECT payload FROM assessment WHERE id=1").fetchone()
        if row is None:
            raise ValueError("No resumable assessment state exists")
        state = json.loads(row[0])
        request = state["request"]
        if request["version"] != VERSION:
            raise ValueError("Assessment version changed; start a fresh run")
        checks = {"database": str(database.resolve()) if database is not None else None,
                  "epic": epic, "as_of": timestamp(cutoff, mandatory=True) if cutoff else None,
                  "offline": offline, "slm_endpoint": slm_endpoint, "claude_model": claude_model,
                  "evidence_limit": evidence_limit}
        if any(value is not None and value != request[name] for name, value in checks.items()):
            raise ValueError("Cannot change saved assessment inputs on resume")
        if manifest_path is not None and read_manifest(manifest_path, request["as_of"]) != request["manifest"]:
            raise ValueError("Cannot change the saved SLM manifest")
    else:
        if not epic or not cutoff:
            raise ValueError("A new assessment requires --epic and --as-of")
        cutoff = timestamp(cutoff, mandatory=True)
        limit = 12 if evidence_limit is None else evidence_limit
        if not 2 <= limit <= 20:
            raise ValueError("Evidence limit must be 2..20")
        manifest = None
        if not offline:
            if manifest_path is None:
                raise ValueError("A live assessment requires a trained SLM --manifest; training is supplied externally")
            manifest = read_manifest(manifest_path, cutoff)
        request = {"version": VERSION, "database": str((database or Path("data/nabu.sqlite")).resolve()),
                   "epic": epic, "as_of": cutoff, "offline": bool(offline), "manifest": manifest,
                   "slm_endpoint": slm_endpoint or "http://127.0.0.1:8080/v1",
                   "claude_model": None if offline else claude_model or os.environ.get("NABU_MODEL"),
                   "evidence_limit": limit}
        if run_dir.exists() and any(run_dir.iterdir()):
            raise ValueError("Run directory must be empty; use --resume or a new directory")
        if Path(request["database"]) == checkpoint:
            raise ValueError("Source and checkpoint database must differ")
        state = {"request": request, "next_stage": "prepare", "events": []}

    def save():
        run_dir.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(checkpoint)) as connection, connection:
            connection.execute("CREATE TABLE IF NOT EXISTS assessment (id INTEGER PRIMARY KEY CHECK(id=1),payload TEXT NOT NULL)")
            connection.execute("INSERT OR REPLACE INTO assessment VALUES (1,?)", (json.dumps(state),))

    # Completed reads and preparation-only runs never require live credentials.
    detector_model = reporter_model = None
    if state["next_stage"] != "done" and not pause_after_prepare:
        if request["offline"]:
            detector_model, reporter_model = detector or OfflineDetector(), reporter or OfflineReporter()
        else:
            detector_model = detector or LocalSLM(request["slm_endpoint"], request["manifest"]["model"])
            reporter_model = reporter or ClaudeReporter(request["claude_model"])

    try:
        if state["next_stage"] == "prepare":
            frozen = freeze_evidence(Path(request["database"]), request["epic"], request["as_of"])
            types = request["manifest"]["risk_types"] if request["manifest"] else ["offline_only"]
            state.update({"input": detector_input(frozen, types, request["evidence_limit"]),
                          "evidence_fingerprint": frozen["evidence_fingerprint"], "next_stage": "detect"})
            state["model_input_fingerprint"] = hashlib.sha256(
                json.dumps(state["input"], sort_keys=True).encode()).hexdigest()
            state["events"].append({"stage": "prepare", "status": "completed"})
            save()
        if pause_after_prepare and state["next_stage"] != "done":
            return {"status": "paused", "analysis_performed": False, "next_stage": state["next_stage"],
                    "run_dir": str(run_dir)}
        if state["next_stage"] == "detect":
            state["detection"] = Detection.model_validate(detector_model.detect(state["input"])).model_dump()
            state["next_stage"] = "validate"
            state["events"].append({"stage": "detect", "status": "completed", "risk_count": len(state["detection"]["risks"])})
            save()
        if state["next_stage"] == "validate":
            state["validated"] = validate_detection(state["detection"], state["input"])
            state["next_stage"] = "present"
            state["events"].append({"stage": "validate", "status": "completed", "rejected": state["validated"]["rejected"]})
            save()
        if state["next_stage"] == "present":
            valid = state["validated"]
            # Claude receives only validated risks and their supplied citations.
            payload = {"plan": state["input"]["plan"], "risks": valid["risks"],
                       "limitations": valid["limitations"], "coverage": state["input"]["coverage"]}
            raw = reporter_model.present(payload) if valid["risks"] else {"sections": []}
            state["presentation"] = validate_presentation(raw, valid["risks"])
            state["next_stage"] = "finalize"
            state["events"].append({"stage": "present", "status": "completed" if valid["risks"] else "skipped_no_risks"})
            save()
        if state["next_stage"] == "finalize":
            state["report"] = {"status": "completed", "architecture": VERSION, "analysis_performed": not request["offline"],
                               "mode": "offline" if request["offline"] else "slm-claude", "epic": request["epic"],
                               "as_of": request["as_of"], "slm_manifest": request["manifest"],
                               "claude_model": request["claude_model"], "evidence_fingerprint": state["evidence_fingerprint"],
                               "model_input_fingerprint": state["model_input_fingerprint"],
                               "risks": state["validated"]["risks"], "rejected": state["validated"]["rejected"],
                               "presentation": state["presentation"], "coverage": state["input"]["coverage"],
                               "evidence_keys": {i["id"]: i["source_key"] for i in state["input"]["prior_work"]},
                               "limitations": [*state["validated"]["limitations"], state["input"]["coverage"]["warning"],
                                               "Exact citations do not establish comparability or prediction accuracy. Claude wording has not been independently verified.",
                                               "Model training provenance is operator-declared; Nabu cannot verify the server weights or unrecorded base-model training data."]}
            state["next_stage"] = "done"
            save()
    except Exception as exc:
        state["events"].append({"stage": state["next_stage"], "status": "failed", "error_type": type(exc).__name__})
        save()
        (run_dir / "events.json").write_text(json.dumps(state["events"], indent=2) + "\n", encoding="utf-8")
        raise
    report = state["report"]
    (run_dir / "review.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (run_dir / "review.md").write_text(markdown(report), encoding="utf-8")
    (run_dir / "events.json").write_text(json.dumps(state["events"], indent=2) + "\n", encoding="utf-8")
    return {**report, "run_dir": str(run_dir)}
