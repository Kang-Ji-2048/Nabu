"""Consensus, independent reference evaluation and temporal dataset safeguards."""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

from ..labelling import encode
from ..pipeline import timestamp
from .classifier import RUBRICS, TARGET_DEFINITION


def read_rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def checked_rows(directory, filename, digest):
    path = directory / filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError(f"Hash mismatch: {path}")
    return read_rows(path)


def dataset_rows(directory):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    inputs = checked_rows(directory, "inputs.jsonl", manifest["files"]["inputs.jsonl"])
    labels = checked_rows(directory, "labels.jsonl", manifest["files"]["labels.jsonl"])
    if len({r["example_id"] for r in inputs}) != len(inputs):
        raise ValueError("Duplicate input example IDs")
    if len({r["example_id"] for r in labels}) != len(labels) or {r["example_id"] for r in inputs} != {r["example_id"] for r in labels}:
        raise ValueError("Outcome labels must match dataset examples exactly")
    return manifest, inputs, {r["example_id"]: r for r in labels}


def prediction_rows(directory, inputs_digest=None):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("target_definition") != TARGET_DEFINITION:
        raise ValueError("Prediction target definition does not match cutoff-time risk classification")
    if inputs_digest and manifest["inputs_sha256"] != inputs_digest:
        raise ValueError("Predictions belong to a different input dataset")
    rows = checked_rows(directory, "predictions.jsonl", manifest["predictions_sha256"])
    if len({row["example_id"] for row in rows}) != len(rows):
        raise ValueError("Duplicate prediction example IDs")
    return manifest, {row["example_id"]: row for row in rows}


def new_output(output):
    if output.exists() and any(output.iterdir()):
        raise ValueError("Use a new or empty output directory")
    output.mkdir(parents=True, exist_ok=True)


def write_bundle(output, files, manifest):
    new_output(output)
    hashes = {}
    for name, rows in files.items():
        body = "".join(encode(row) + "\n" for row in rows)
        (output / name).write_text(body, encoding="utf-8", newline="\n")
        hashes[name] = hashlib.sha256(body.encode()).hexdigest()
    report = {**manifest, "files": hashes}
    (output / "manifest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return {**report, "output": str(output.resolve())}


def combine_labels(dataset, predictions, output, min_sources=2):
    """Only agree on identical targets; future outcome proxies never vote."""
    if min_sources < 2:
        raise ValueError("Consensus requires at least two distinct model sources")
    manifest, inputs, outcomes = dataset_rows(dataset)
    sources, identities = [], set()
    ids = {row["example_id"] for row in inputs}
    for directory in predictions:
        source_manifest, rows = prediction_rows(directory, manifest["files"]["inputs.jsonl"])
        if set(rows) - ids:
            raise ValueError("Prediction contains an unknown example")
        resolved = {row.get("served_model") or row["model"] for row in rows.values()}
        if len(resolved) > 1:
            raise ValueError("A model source changed served models within its batch")
        identity = (source_manifest.get("provider", "jev"), next(iter(resolved), source_manifest["model"]))
        if identity in identities:
            raise ValueError("Repeated runs or aliases of the same model cannot count as independent sources")
        identities.add(identity)
        sources.append((identity, rows))
    if len(sources) < min_sources:
        raise ValueError("Not enough distinct model sources for consensus")
    records, training, counts = [], [], Counter()
    for example in inputs:
        eid = example["example_id"]
        decisions, targets = {}, {}
        for risk in RUBRICS:
            votes = [{"source": list(identity), **rows[eid]["classification"][risk]}
                     for identity, rows in sources if eid in rows]
            values = [vote["target"] for vote in votes if vote["target"] is not None]
            # Any explicit opposing vote vetoes; abstentions do not count as support.
            accepted = len(values) >= min_sources and len(set(values)) == 1
            target = values[0] if accepted else None
            reason = "agreement" if accepted else "disagreement" if len(set(values)) > 1 else "insufficient_support"
            decisions[risk] = {"target": target, "reason": reason, "votes": votes,
                               "later_outcome_proxy": outcomes[eid]["targets"].get(risk)}
            targets[risk] = target
            counts[f"{risk}:{reason}"] += 1
        records.append({"example_id": eid, "item_id": example["input"]["ticket"]["id"],
                        "target_definition": TARGET_DEFINITION, "targets": targets, "decisions": decisions,
                        "reviewed": False, "label_kind": "weak_consensus"})
        if any(value is not None for value in targets.values()):
            training.append({"example_id": eid, "input": example["input"], "targets": targets,
                             "label_kind": "weak_consensus"})
    return write_bundle(output, {"labels.jsonl": records, "training.jsonl": training},
                        {"version": "nabu.label-consensus.v1", "target_definition": TARGET_DEFINITION,
                         "training_readiness": "unvalidated_weak_supervision",
                         "inputs_sha256": manifest["files"]["inputs.jsonl"], "min_sources": min_sources,
                         "sources": [list(i) for i in sorted(identities)], "counts": dict(counts),
                         "examples": len(inputs), "training_examples": len(training),
                         "policy": "Unanimous accepted votes from distinct models; outcomes remain separate auxiliary targets."})


def make_reference(dataset, predictions, output, size=100):
    if size < 1:
        raise ValueError("Reference size must be positive")
    manifest, inputs, outcomes = dataset_rows(dataset)
    predictions = prediction_rows(predictions, manifest["files"]["inputs.jsonl"])[1] if predictions else {}
    buckets = defaultdict(list)
    lookup = {r["example_id"]: r for r in inputs}
    for row in inputs:
        eid = row["example_id"]
        strata = ["random"]
        if outcomes[eid]["state"] == "observed_signal":
            strata.append("outcome_signal")
        if not row["input"].get("context", {}).get("plans"):
            strata.append("missing_plan_context")
        if eid in predictions:
            for risk, result in predictions[eid]["classification"].items():
                strata.append(f"{risk}:{result['target']}")
        for stratum in strata:
            buckets[stratum].append(eid)
    for values in buckets.values():
        values.sort(key=lambda eid: hashlib.sha256(eid.encode()).hexdigest())
    selected = []
    while len(selected) < min(size, len(inputs)):
        for name in sorted(buckets):
            while buckets[name] and buckets[name][-1] in selected:
                buckets[name].pop()
            if buckets[name] and len(selected) < size:
                selected.append(buckets[name].pop())
    reference = [{"example_id": eid, "target_definition": TARGET_DEFINITION,
                  "input": lookup[eid]["input"], "reviewed": False, "reviewer": "",
                  "targets": {risk: None for risk in RUBRICS}, "notes": ""} for eid in selected]
    return write_bundle(output, {"reference.jsonl": reference},
                        {"version": "nabu.reference-sample.v1", "inputs_sha256": manifest["files"]["inputs.jsonl"],
                         "examples": len(reference), "sampling": "deterministic_round_robin_stratified",
                         "population_estimate": False,
                         "instructions": "Independent reviewers label explicit concerns from input only; do not consult predictions/outcomes. Null means unjudgeable. Set reviewed=true and reviewer identity after review."})


def evaluate_labels(dataset, predictions, reference, output):
    manifest, inputs, _ = dataset_rows(dataset)
    _, predicted = prediction_rows(predictions, manifest["files"]["inputs.jsonl"])
    ids = {r["example_id"] for r in inputs}
    original = {r["example_id"]: r["input"] for r in inputs}
    references = read_rows(reference)
    if len({r["example_id"] for r in references}) != len(references):
        raise ValueError("Duplicate reference example IDs")
    approved = []
    for row in references:
        if row["example_id"] not in ids or row.get("target_definition") != TARGET_DEFINITION:
            raise ValueError("Reference example or target definition does not match")
        if "input" in row and row["input"] != original[row["example_id"]]:
            raise ValueError("Reference input differs from the frozen dataset")
        if row.get("reviewed") is not True:
            continue
        if not isinstance(row.get("reviewer"), str) or not row["reviewer"].strip():
            raise ValueError("Reviewed references require a reviewer identity")
        if set(row["targets"]) != set(RUBRICS) or any(v is not None and (type(v) is not int or v not in (0, 1)) for v in row["targets"].values()):
            raise ValueError("Reference targets must be 0, 1 or null for every risk type")
        approved.append(row)
    if not approved:
        raise ValueError("No independently reviewed references; label accuracy cannot be evaluated")
    metrics = {}
    for risk in RUBRICS:
        c = Counter()
        scored = []
        for row in approved:
            truth = row["targets"][risk]
            if truth is None:
                c["unjudgeable"] += 1
                continue
            c["judgeable"] += 1
            prediction = predicted.get(row["example_id"], {}).get("classification", {}).get(risk)
            value = prediction["target"] if prediction else None
            if value is None:
                c["abstained"] += 1
                if truth == 1:
                    c["missed_positive_abstention"] += 1
            else:
                c["accepted"] += 1
                c["tp" if value == truth == 1 else "tn" if value == truth == 0 else "fp" if value else "fn"] += 1
            if prediction:
                scored.append((prediction["confidence"], prediction["choice"], truth,
                               "missing_or_invalid_evidence" not in prediction.get("abstention_reasons", []),
                               prediction.get("evidence_confidence", 0)))
        def ratio(n, d):
            return n / d if d else None
        precision = ratio(c["tp"], c["tp"] + c["fp"])
        recall = ratio(c["tp"], c["tp"] + c["fn"] + c["missed_positive_abstention"])
        sweep = []
        for threshold in (0.5, 0.7, 0.8, 0.9, 0.95):
            accepted = [(choice == "risk", truth) for confidence, choice, truth, evidence_ok, evidence_conf in scored
                        if confidence >= threshold and evidence_conf >= threshold and evidence_ok and choice != "insufficient_evidence"]
            tp = sum(value and truth == 1 for value, truth in accepted)
            fp = sum(value and truth == 0 for value, truth in accepted)
            sweep.append({"threshold": threshold, "precision": ratio(tp, tp + fp),
                          "coverage": ratio(len(accepted), c["judgeable"]), "accepted": len(accepted)})
        metrics[risk] = {"counts": dict(c), "precision": precision, "recall_including_abstentions": recall,
                         "coverage": ratio(c["accepted"], c["judgeable"]),
                         "threshold_sweep": sweep}
    return write_bundle(output, {}, {"version": "nabu.label-evaluation.v1", "metrics": metrics,
                                    "reviewed_examples": len(approved), "pending_examples": len(references) - len(approved),
                                    "reference_sha256": hashlib.sha256(reference.read_bytes()).hexdigest(),
                                    "limitations": ["Metrics describe the reviewed sample, not population prevalence.",
                                                    "Tune thresholds on validation references; keep test references separate.",
                                                    "Human review status and independence are operator declarations."]})


def split_data(datasets, output, train_through, validation_through):
    """Chronological partitions with related/duplicate groups retained in one split."""
    import re
    train_end = timestamp(train_through, mandatory=True)
    validation_end = timestamp(validation_through, mandatory=True)
    if validation_end <= train_end:
        raise ValueError("Validation boundary must follow the training boundary")
    examples, labels, relations = {}, {}, []
    fingerprints = []
    for directory in datasets:
        manifest, rows, outcomes = dataset_rows(directory)
        fingerprints.append(manifest["dataset_sha256"])
        for row in rows:
            eid = row["example_id"]
            if eid in examples:
                raise ValueError("Repeated input examples across datasets")
            examples[eid] = row
            labels[eid] = outcomes[eid]
        if "split-relations.jsonl" in manifest["files"]:
            relations.extend(checked_rows(directory, "split-relations.jsonl", manifest["files"]["split-relations.jsonl"]))
    parent = {}
    def find(key):
        parent.setdefault(key, key)
        if parent[key] != key:
            parent[key] = find(parent[key])
        return parent[key]
    def union(keys):
        keys = list(keys)
        if not keys:
            return
        root = find(keys[0])
        for key in keys[1:]:
            other = find(key)
            parent[other] = root
    exact, titles = defaultdict(list), defaultdict(list)
    for eid, row in examples.items():
        item = row["input"]["ticket"]
        union([item["id"], *row.get("group_item_ids", [])])
        # Exclude unknown text and identifiers from duplicate detection.
        text = " ".join(str(item["fields"].get(field) or "") for field in ("title", "description", "acceptance_criteria")
                        if field not in item["unknown_fields"])
        normal = " ".join(re.findall(r"\w+", text.casefold()))
        if normal:
            exact[normal].append(item["id"])
        title = " ".join(re.findall(r"\w+", str(item["fields"].get("title") or "").casefold()))
        if "title" not in item["unknown_fields"] and len(title) >= 25:
            titles[title].append(item["id"])
    for group in [*exact.values(), *titles.values()]:
        union(group)
    for relationship in relations:
        union(relationship["item_ids"])
    desired, group_splits = {}, defaultdict(set)
    for eid, row in examples.items():
        cutoff = row["input"]["as_of"]
        horizon = labels[eid]["observation_window"]["through"]
        if cutoff <= train_end and horizon <= train_end:
            split = "train"
        elif train_end < cutoff <= validation_end and horizon <= validation_end:
            split = "validation"
        elif cutoff > validation_end:
            split = "test"
        else:
            split = "quarantine"
        desired[eid] = split
        if split != "quarantine":
            group_splits[find(row["input"]["ticket"]["id"])].add(split)
    rank = {"train": 0, "validation": 1, "test": 2}
    assignments, files, counts, class_counts = [], {}, Counter(), defaultdict(Counter)
    for split in ("train", "validation", "test"):
        files[f"{split}-inputs.jsonl"] = []
        files[f"{split}-outcomes.jsonl"] = []
    for eid, row in examples.items():
        group = find(row["input"]["ticket"]["id"])
        split = desired[eid]
        reason = "observation_window_crosses_boundary" if split == "quarantine" else "chronological"
        if split != "quarantine" and split != max(group_splits[group], key=rank.get):
            split, reason = "quarantine", "related_or_duplicate_group_reserved_for_later_split"
        group_id = hashlib.sha256(group.encode()).hexdigest()
        assignments.append({"example_id": eid, "split": split, "group_id": group_id, "reason": reason})
        counts[split] += 1
        if split != "quarantine":
            files[f"{split}-inputs.jsonl"].append(row)
            files[f"{split}-outcomes.jsonl"].append(labels[eid])
            for risk, target in labels[eid]["targets"].items():
                class_counts[split][f"{risk}:{target}"] += 1
    files["assignments.jsonl"] = assignments
    missing = Counter(field for row in examples.values() for field in row["input"]["ticket"]["unknown_fields"])
    warnings = []
    for split in ("train", "validation", "test"):
        if counts[split] == 0:
            warnings.append(f"{split} has no examples after grouping and time checks")
        for risk in ("estimation", "dependency", "rework"):
            if class_counts[split][f"{risk}:1"] < 20:
                warnings.append(f"{split}/{risk} has fewer than 20 outcome-proxy positives; threshold is a coverage warning, not a statistical guarantee")
    return write_bundle(output, files, {"version": "nabu.temporal-splits.v1", "datasets": fingerprints,
                                       "train_through": train_end, "validation_through": validation_end,
                                       "counts": dict(counts), "outcome_class_counts": {k: dict(v) for k, v in class_counts.items()},
                                       "missing_field_counts": dict(missing),
                                       "exact_duplicate_groups": sum(len(set(v)) > 1 for v in exact.values()),
                                       "matching_title_groups": sum(len(set(v)) > 1 for v in titles.values()),
                                       "missing_plan_context": sum(not r["input"].get("context", {}).get("plans") for r in examples.values()),
                                       "warnings": warnings,
                                       "policy": "Group repeated tickets, observed epic members, exact normalized text, matching long titles and snapshot relations. Reserve each group for its latest partition; quarantine earlier rows. Snapshot links never enter features.",
                                       "limitations": ["Semantic near duplicates beyond matching normalized titles/text are not detected.",
                                                       "Unknown relationships cannot be grouped.",
                                                       "Outcome labels are auxiliary proxies, not classifier ground truth."]})
