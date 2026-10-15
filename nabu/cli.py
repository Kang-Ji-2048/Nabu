import argparse
import json
from pathlib import Path
import sqlite3
import sys

from .extract import export_mysql
from .dump import export_dump, profile_dump
from .pipeline import load
from .replay import write_replay
from .risk.schema import CONTRACT_NAMES


def main(argv=None):
    parser = argparse.ArgumentParser(description="Nabu delivery risk review and historical data pipeline")
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("extract", help="Export one project from restored TAWOS MySQL")
    export.add_argument("--project", required=True)
    export.add_argument("--output", type=Path, required=True)
    dump = commands.add_parser("extract-dump", help="Export one project directly from the TAWOS SQL dump")
    dump.add_argument("--input", type=Path, required=True)
    dump.add_argument("--project", required=True)
    dump.add_argument("--output", type=Path, required=True)
    profile = commands.add_parser("profile-dump", help="Compare project coverage in the TAWOS SQL dump")
    profile.add_argument("--input", type=Path, required=True)
    profile.add_argument("--report", type=Path)
    replay = commands.add_parser("replay", help="Reconstruct a historical plan with a separate outcome reveal")
    replay.add_argument("--database", type=Path, default=Path("data/nabu.sqlite"))
    replay.add_argument("--epic", required=True)
    replay.add_argument("--as-of", required=True, help="Inclusive ISO timestamp; timezone-naive values are UTC")
    replay.add_argument("--output", type=Path, required=True)
    review = commands.add_parser("review", help="Run/resume a LangGraph historical gap investigation")
    review.add_argument("--database", type=Path)
    review.add_argument("--epic")
    review.add_argument("--as-of")
    review.add_argument("--run-dir", type=Path, required=True)
    review.add_argument("--offline", action="store_true", default=None, help="Scripted smoke test; no AI analysis or API calls")
    review.add_argument("--model", help="Anthropic model ID; defaults to NABU_MODEL")
    review.add_argument("--resume", action="store_true")
    review.add_argument("--pause-after-prepare", action="store_true", help="Save the historical evidence then stop before investigation")
    review.add_argument("--max-model-calls", type=int, default=10)
    review.add_argument("--max-tool-calls", type=int, default=20)
    review.add_argument("--max-rounds", type=int, default=2)
    review.add_argument("--retrieval", choices=("lexical", "semantic"))
    review.add_argument("--embedding-model-dir", type=Path)
    review.add_argument("--embedding-cache", type=Path)
    assess = commands.add_parser("assess", help="Detect risks with a trained local SLM, then present them with Claude")
    assess.add_argument("--database", type=Path)
    assess.add_argument("--epic")
    assess.add_argument("--as-of")
    assess.add_argument("--run-dir", type=Path, required=True)
    assess.add_argument("--manifest", type=Path, help="Externally trained SLM provenance manifest")
    assess.add_argument("--slm-endpoint", help="Loopback OpenAI-compatible server URL ending in /v1")
    assess.add_argument("--model", help="Claude model ID; defaults to NABU_MODEL")
    assess.add_argument("--evidence-limit", type=int)
    assess.add_argument("--offline", action="store_true", default=None, help="Scripted wiring test; no AI analysis")
    assess.add_argument("--resume", action="store_true")
    assess.add_argument("--pause-after-prepare", action="store_true")
    slm_schema = commands.add_parser("slm-schema", help="Export the v1 detector or versioned risk workflow JSON schemas")
    slm_schema.add_argument("--output", type=Path, required=True)
    slm_schema.add_argument("--contract", choices=CONTRACT_NAMES, default="detection",
                            help="Defaults to the trained v1 detector; workflow exports the new assessment, policy, manager and report contracts")
    prepare = commands.add_parser("prepare-model", help="Download and verify the pinned local embedding model")
    prepare.add_argument("--model-dir", type=Path, default=Path("data/models/bge-small-en-v1.5"))
    categories = commands.add_parser("discover-categories", help="Discover work categories from local ticket embeddings")
    categories.add_argument("--database", type=Path, default=Path("data/nabu.sqlite"))
    categories.add_argument("--project", required=True)
    categories.add_argument("--as-of")
    categories.add_argument("--output", type=Path, required=True)
    categories.add_argument("--model-dir", type=Path, default=Path("data/models/bge-small-en-v1.5"))
    categories.add_argument("--cache", type=Path, default=Path("data/semantic/embeddings.sqlite"))
    categories.add_argument("--min-cluster-size", type=int, default=15)
    categories.add_argument("--min-samples", type=int, default=5)
    search = commands.add_parser("search-categories", help="Match text to discovered categories and similar tickets")
    search.add_argument("--index-dir", type=Path, required=True)
    search.add_argument("--query", required=True)
    search.add_argument("--limit", type=int, default=5)
    ingest = commands.add_parser("load", help="Normalize a TAWOS JSONL export into SQLite")
    ingest.add_argument("--input", type=Path, required=True)
    ingest.add_argument("--database", type=Path, default=Path("data/nabu.sqlite"))
    ingest.add_argument("--mappings", type=Path)
    ingest.add_argument("--report", type=Path)
    dataset = commands.add_parser("build-slm-dataset", help="Build frozen examples and reviewed SFT partitions")
    dataset.add_argument("--database", type=Path, required=True)
    dataset.add_argument("--cases", type=Path, required=True)
    dataset.add_argument("--output", type=Path, required=True)
    dataset.add_argument("--train-before", required=True)
    dataset.add_argument("--eval-before", required=True)
    dataset.add_argument("--limit", type=int, default=12)
    baseline = commands.add_parser("evaluate-slm-baseline", help="Evaluate an explicitly untrained Ollama baseline")
    baseline.add_argument("--dataset", type=Path, required=True)
    baseline.add_argument("--output", type=Path, required=True)
    baseline.add_argument("--model", required=True, help="Exact Ollama model name")
    baseline.add_argument("--checkpoint", default="Qwen/Qwen3-4B-Instruct-2507", help="Expected source checkpoint; alias identity still requires separate verification")
    baseline.add_argument("--slm-endpoint", default="http://127.0.0.1:11434/v1")
    baseline.add_argument("--max-input-bytes", type=int, default=24000)
    baseline.add_argument("--max-tokens", type=int, default=4096)
    dataset.add_argument("--risk-types", nargs="+", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "build-slm-dataset":
            from .slm import build_dataset
            result = build_dataset(args.database, args.cases, args.output, train_before=args.train_before,
                                   eval_before=args.eval_before, risk_types=args.risk_types, limit=args.limit)
        elif args.command == "evaluate-slm-baseline":
            from .slm import evaluate_baseline
            result = evaluate_baseline(args.dataset, args.output, model=args.model, checkpoint=args.checkpoint, endpoint=args.slm_endpoint,
                                       max_input_bytes=args.max_input_bytes, max_tokens=args.max_tokens)
        elif args.command == "extract":
            result = export_mysql(args.project, args.output)
        elif args.command == "extract-dump":
            result = export_dump(args.input, args.project, args.output)
        elif args.command == "profile-dump":
            if args.report and args.report.resolve() == args.input.resolve():
                raise ValueError("Report must not overwrite input")
            result = profile_dump(args.input)
            if args.report:
                args.report.parent.mkdir(parents=True, exist_ok=True)
                args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        elif args.command == "replay":
            result = write_replay(args.database, args.epic, args.as_of, args.output)
        elif args.command == "slm-schema":
            from .risk.schema import risk_schema
            schema, version = risk_schema(args.contract)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(json.dumps(schema, indent=2) + "\n")
            result = {"schema": str(args.output.resolve()), "version": version}
        elif args.command == "assess":
            try:
                from .risk.runner import run_assessment
            except ImportError as exc:
                raise ValueError('Install agent dependencies: pip install -e ".[agents]"') from exc
            try:
                result = run_assessment(args.database, args.epic, args.as_of, args.run_dir,
                                        offline=args.offline, manifest_path=args.manifest,
                                        slm_endpoint=args.slm_endpoint, claude_model=args.model,
                                        evidence_limit=args.evidence_limit, resume=args.resume,
                                        pause_after_prepare=args.pause_after_prepare)
            except (ValueError, OSError, sqlite3.Error):
                raise
            except Exception as exc:
                raise ValueError(f"Assessment failed ({type(exc).__name__}); check {args.run_dir} and use --resume after fixing the cause") from exc
        elif args.command == "review":
            try:
                from .agents.runner import run_review
            except ImportError as exc:
                raise ValueError('Install agent dependencies: pip install -e ".[agents]"') from exc
            try:
                result = run_review(args.database, args.epic, args.as_of, args.run_dir,
                                    offline=args.offline, model_id=args.model, resume=args.resume,
                                    pause_after_prepare=args.pause_after_prepare,
                                    max_model_calls=args.max_model_calls, max_tool_calls=args.max_tool_calls,
                                    max_rounds=args.max_rounds, retrieval=args.retrieval,
                                    embedding_model_dir=args.embedding_model_dir, embedding_cache=args.embedding_cache)
            except ImportError as exc:
                raise ValueError('Install semantic dependencies: pip install -e ".[agents,semantic]"') from exc
            except (ValueError, OSError, sqlite3.Error):
                raise
            except Exception as exc:
                raise ValueError(f"Review failed ({type(exc).__name__}); saved state is in {args.run_dir}. Use --resume to continue.") from exc
        elif args.command == "prepare-model":
            from .semantic.encoder import prepare_model
            result = prepare_model(args.model_dir)
        elif args.command == "discover-categories":
            from .semantic.categories import write_discovery
            result = write_discovery(args.database, args.project, args.output, cutoff=args.as_of,
                                     model_dir=args.model_dir, cache=args.cache,
                                     min_cluster_size=args.min_cluster_size, min_samples=args.min_samples)
        elif args.command == "search-categories":
            from .semantic.categories import search_inventory
            result = search_inventory(args.index_dir, args.query, limit=args.limit)
        else:
            if args.report and args.report.resolve() in {args.input.resolve(), args.database.resolve()}:
                raise ValueError("Report path must differ from input and database")
            result = load(args.input, args.database, args.mappings)
            if args.report:
                args.report.parent.mkdir(parents=True, exist_ok=True)
                args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
    except ImportError as exc:
        print('Nabu failed: install semantic dependencies with pip install -e ".[semantic]"', file=sys.stderr)
        raise SystemExit(1) from exc
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(f"Nabu failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    if result.get("rejected", 0):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
