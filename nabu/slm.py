"""Cutoff-bound supervised examples and explicitly untrained baseline evaluation."""
import json
from urllib.request import Request

from .risk.contracts import Detection
from .risk.runner import detector_input, validate_detection
from .risk.models import DETECT_PROMPT, LocalSLM
from .agents.evidence import freeze_evidence
from .pipeline import timestamp

CHECKPOINT = "Qwen/Qwen3-4B-Instruct-2507"
SUPPORTED_CHECKPOINTS = (CHECKPOINT, "Qwen/Qwen3-8B", "Qwen/Qwen3-14B")
PROMPT = DETECT_PROMPT

def messages(payload):
    return [{"role": "system", "content": PROMPT},
            {"role": "user", "content": json.dumps(payload)}]


def build_dataset(database, cases_path, output, *, train_before, eval_before, risk_types, limit=12):
    """Cases carry labels separately; only frozen allowlisted fields enter messages."""
    train_before, eval_before = timestamp(train_before, mandatory=True), timestamp(eval_before, mandatory=True)
    if train_before >= eval_before:
        raise ValueError("train-before must precede eval-before")
    if not 2 <= limit <= 20 or not risk_types or len(set(risk_types)) != len(risk_types) or any(not t.strip() for t in risk_types):
        raise ValueError("Evidence limit must be 2..20 and risk types must be nonempty and unique")
    cases = [json.loads(line) for line in cases_path.read_text().splitlines() if line.strip()]
    if not cases:
        raise ValueError("Cases file is empty")
    rows, groups, seen = [], {}, set()
    for case in cases:
        case_id = case["id"]
        if case_id in seen:
            raise ValueError("Case IDs must be unique")
        seen.add(case_id)
        frozen = freeze_evidence(database, case["epic"], case["as_of"])
        payload = detector_input(frozen, risk_types, limit)
        cutoff = frozen["plan"]["as_of"]
        split = "train" if cutoff < train_before else "validation" if cutoff < eval_before else "test"
        # Related roots and overlapping plan members must stay in the same partition.
        related = {case.get("group", case["epic"]), *(item["id"] for item in [payload["plan"]["root"], *payload["plan"]["members"]])}
        for group in related:
            if group in groups and groups[group] != split:
                raise ValueError(f"Related group {group!r} crosses time partitions; adjust cutoffs or cases")
            groups[group] = split
        row = {"id": case_id, "epic": case["epic"], "group": case.get("group", case["epic"]), "as_of": cutoff,
               "split": split, "base_checkpoint": CHECKPOINT, "evidence_fingerprint": frozen["evidence_fingerprint"],
               "input": payload, "messages": messages(payload), "review_status": "draft"}
        if "target" in case:
            if not isinstance(case.get("reviewer"), str) or not case["reviewer"].strip() or case.get("review_status") != "approved":
                raise ValueError("Targets require review_status=approved and a named human reviewer")
            target = Detection.model_validate(case["target"]).model_dump()
            errors = validate_detection(target, payload)["rejected"]
            if errors:
                raise ValueError(f"Invalid target citations in {case_id}: {errors}")
            row.update(target=target, reviewer=case["reviewer"], review_status="approved")
            row["messages"].append({"role": "assistant", "content": json.dumps(target, ensure_ascii=False)})
        rows.append(row)
    if output.exists():
        raise ValueError("Dataset output already exists")
    output.mkdir(parents=True)
    for split in ("train", "validation", "test"):
        approved = [row for row in rows if row["split"] == split and row["review_status"] == "approved"]
        (output / f"{split}.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in approved))
    (output / "cases.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    return {"cases": len(rows), "approved": sum(row["review_status"] == "approved" for row in rows), "output": str(output)}


def ollama_completion(endpoint, model, prompt, max_input_bytes, max_tokens):
    # Byte cap is a conservative transport guard, not a tokenizer estimate.
    body = json.dumps({"model": model, "messages": prompt, "temperature": 0,
                       "max_tokens": max_tokens, "response_format": {"type": "json_object"}}).encode()
    if len(body) > max_input_bytes:
        raise ValueError("Payload exceeds byte budget; reduce retrieval or increase the explicit budget. No evidence was truncated.")
    adapter = LocalSLM(endpoint, model)
    request = Request(adapter.endpoint, data=body, headers={"Content-Type": "application/json"})
    from urllib.request import build_opener, ProxyHandler
    from .risk.models import NoRedirect
    with build_opener(ProxyHandler({}), NoRedirect()).open(request, timeout=180) as response:
        raw = response.read(1_000_001)
    if len(raw) > 1_000_000:
        raise ValueError("SLM response exceeded size limit")
    result = json.loads(raw)
    choice = result["choices"][0]
    if choice.get("finish_reason") != "stop" or result.get("model") != model:
        raise ValueError("Incomplete response or mismatched model alias")
    return json.loads(choice["message"]["content"])


def evaluate_baseline(dataset, output, *, model, endpoint="http://127.0.0.1:11434/v1", max_input_bytes=24000, max_tokens=4096, completion=None):
    if max_input_bytes < 1 or max_tokens < 1:
        raise ValueError("Budgets must be positive")
    if output.exists() or output.resolve() == dataset.resolve():
        raise ValueError("Choose a new report output")
    rows = [json.loads(line) for line in dataset.read_text().splitlines() if line.strip()]
    if not rows:
        raise ValueError("Evaluation dataset is empty")
    results = []
    for row in rows:
        if row["split"] not in {"validation", "test"}:
            raise ValueError("Baseline evaluation accepts only validation/test cases")
        payload = row["input"]
        entry = {"id": row["id"], "human_assessment": {"useful_findings": None, "false_alarms": None}}
        try:
            raw = (completion or ollama_completion)(endpoint, model, messages(payload), max_input_bytes, max_tokens)
            submission = Detection.model_validate(raw).model_dump()
            validated = validate_detection(submission, payload)
            valid, errors = validated["risks"], validated["rejected"]
            entry.update(submission=submission, valid_findings=len(valid), proposed_findings=len(submission["risks"]), citation_errors=errors, schema_valid=True)
        except (ValueError, OSError, KeyError, IndexError, TypeError) as exc:
            entry.update(schema_valid=False, error=str(exc))
        results.append(entry)
    proposed = sum(row.get("proposed_findings", 0) for row in results)
    report = {"mode": "untrained_baseline", "trained": False, "expected_base_checkpoint": CHECKPOINT,
              "model": model, "checkpoint_identity_verified": False, "endpoint": endpoint,
              "metrics": {"cases": len(results), "schema_valid_cases": sum(row["schema_valid"] for row in results),
                          "citation_valid_finding_fraction": sum(row.get("valid_findings", 0) for row in results) / proposed if proposed else None,
                          "useful_findings": None, "false_alarms": None},
              "limitations": ["Human assessment of usefulness and false alarms is pending.", "Byte budget is not a token count; verify the Ollama template, checkpoint identity and context capacity separately."], "results": results}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report
