"""Synthetic development controls, deliberately separate from real-data evaluation."""
import argparse
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.risk.classifier import validate_result
from nabu.risk.label_evidence import classifier_payload
from nabu.risk.laya import LayaClassifier

CASES = [
    ("dependency", 1, "Deployment cannot proceed because the external API credentials have not been issued. This remains a blocker."),
    ("scope_gap", 1, "The agreed release requires rollback support. No rollback implementation or acceptance tests have been planned; this is still missing."),
    ("estimation", 1, "The effort estimate is unreliable because the migration complexity is unknown. We cannot commit to the delivery date until the investigation is complete."),
    ("rework", 1, "The existing migration corrupts records. We must discard the current implementation and repeat the migration work before delivery."),
    ("dependency", 0, "The previously missing API credentials have now been issued and tested. That deployment blocker is resolved."),
    ("dependency", None, "Add a configuration option for the API connector."),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=Path("data/models/laya-typed-decisions"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    teacher = LayaClassifier(args.model)
    results = []
    for number, (risk, expected, text) in enumerate(CASES):
        item = {"id": f"CONTROL-{number}", "source_key": f"CONTROL-{number}",
                "fields": {"title": "Synthetic development control", "description": text, "acceptance_criteria": None},
                "unknown_fields": ["acceptance_criteria"]}
        payload = classifier_payload({"input": {"as_of": "2021-01-01", "ticket": item}})
        started = time.perf_counter()
        raw = teacher.classify(payload)
        validated = validate_result(raw, 0.8, payload)
        answer = validated[risk]
        result = {"risk_type": risk, "expected": expected, "text": text,
                  "result": answer, "seconds": round(time.perf_counter() - started, 3)}
        results.append(result)
        print(json.dumps({"case": number, "risk": risk, "choice": answer["choice"],
                          "confidence": answer["confidence"], "accepted_target": answer["target"]}), flush=True)
    teacher.close()
    report = {"purpose": "Synthetic development controls; not held-out accuracy on TAWOS",
              "model": teacher.served_model, "cases": results,
              "accepted": sum(r["result"]["target"] is not None for r in results),
              "correct_raw_choices": sum(r["result"]["choice"] == ("risk" if r["expected"] == 1 else "no_risk" if r["expected"] == 0 else "insufficient_evidence") for r in results)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
