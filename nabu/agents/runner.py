import json
import os
from pathlib import Path

from langgraph.checkpoint.sqlite import SqliteSaver

from ..pipeline import timestamp
from .graph import VERSION, build_graph
from .models import OfflineSmokeModel, make_model


def run_review(database, epic, cutoff, run_dir: Path, *, offline=None, model_id=None,
               resume=False, pause_after_prepare=False, model=None,
               max_model_calls=10, max_tool_calls=20, max_rounds=2):
    run_dir = run_dir.resolve()
    checkpoint = run_dir / "checkpoints.sqlite"
    config = {"configurable": {"thread_id": "review"}, "recursion_limit": 500}
    if not resume:
        if not epic or not cutoff:
            raise ValueError("A new review requires --epic and --as-of")
        if not 1 <= max_model_calls <= 100 or not 1 <= max_tool_calls <= 200 or not 1 <= max_rounds <= 3:
            raise ValueError("Limits: model calls 1..100, tool calls 1..200, rounds 1..3")
        mode = "offline" if offline else "anthropic"
        model_id = "offline-smoke-v1" if offline else model_id or os.environ.get("NABU_MODEL")
        request = {"version": VERSION, "database": str((database or Path("data/nabu.sqlite")).resolve()),
                   "epic": epic, "as_of": timestamp(cutoff, mandatory=True), "mode": mode, "model": model_id,
                   "max_model_calls": max_model_calls, "max_tool_calls": max_tool_calls, "max_rounds": max_rounds}
        runtime_model = model or make_model(mode, model_id)
        if Path(request["database"]) == checkpoint:
            raise ValueError("Checkpoint and source database must differ")
        if run_dir.exists() and any(run_dir.iterdir()):
            raise ValueError("Run directory is not empty; use --resume or a new directory")
        run_dir.mkdir(parents=True, exist_ok=True)
    elif not checkpoint.exists():
        raise ValueError("No saved checkpoint exists in the run directory")

    with SqliteSaver.from_conn_string(str(checkpoint)) as saver:
        if resume:
            snapshot = build_graph(OfflineSmokeModel(), saver).get_state(config)
            if not snapshot.values or "request" not in snapshot.values:
                raise ValueError("No resumable review state was saved")
            request = snapshot.values["request"]
            if request["version"] != VERSION:
                raise ValueError("Workflow version changed; create a new review")
            if epic and epic != request["epic"] or cutoff and timestamp(cutoff, mandatory=True) != request["as_of"]:
                raise ValueError("Cannot change the epic or cutoff of a saved review")
            if database is not None and str(database.resolve()) != request["database"]:
                raise ValueError("Cannot change the source database locator of a saved review")
            if model_id and model_id != request["model"] or offline is not None and ("offline" if offline else "anthropic") != request["mode"]:
                raise ValueError("Cannot change the model/mode of a saved review")
            runtime_model = model or (make_model(request["mode"], request["model"]) if snapshot.next else OfflineSmokeModel())
        graph = build_graph(runtime_model, saver, pause_after_prepare=pause_after_prepare)
        if resume and not snapshot.next:
            state = snapshot.values
        else:
            try:
                state = graph.invoke(None if resume else {"request": request}, config)
            except Exception as exc:
                failed = graph.get_state(config)
                failure = {"status": "failed", "error_type": type(exc).__name__,
                           "epic": request["epic"], "as_of": request["as_of"],
                           "next_stages": list(failed.next), "checkpoint_retained": True}
                (run_dir / "review.json").write_text(json.dumps(failure, indent=2) + "\n", encoding="utf-8")
                (run_dir / "events.json").write_text(json.dumps(failed.values.get("events", []), indent=2) + "\n", encoding="utf-8")
                raise
        saved = graph.get_state(config)
        if saved.next:
            report = {"status": "paused", "mode": request["mode"], "analysis_performed": False,
                      "epic": request["epic"], "as_of": request["as_of"], "next_stages": list(saved.next),
                      "evidence_fingerprint": state.get("evidence_fingerprint")}
        else:
            report = state["report"]
        (run_dir / "review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (run_dir / "events.json").write_text(json.dumps(state.get("events", []), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (run_dir / "workflow.mmd").write_text(graph.get_graph().draw_mermaid() + "\n", encoding="utf-8")
    return {**report, "run_dir": str(run_dir)}
