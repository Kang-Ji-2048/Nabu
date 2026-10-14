import argparse
import json
from pathlib import Path
import sqlite3
import sys

from .extract import export_mysql
from .dump import export_dump, profile_dump
from .pipeline import load
from .replay import write_replay


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
    ingest = commands.add_parser("load", help="Normalize a TAWOS JSONL export into SQLite")
    ingest.add_argument("--input", type=Path, required=True)
    ingest.add_argument("--database", type=Path, default=Path("data/nabu.sqlite"))
    ingest.add_argument("--mappings", type=Path)
    ingest.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "extract":
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
                                    max_rounds=args.max_rounds)
            except (ValueError, OSError, sqlite3.Error):
                raise
            except Exception as exc:
                raise ValueError(f"Review failed ({type(exc).__name__}); saved state is in {args.run_dir}. Use --resume to continue.") from exc
        else:
            if args.report and args.report.resolve() in {args.input.resolve(), args.database.resolve()}:
                raise ValueError("Report path must differ from input and database")
            result = load(args.input, args.database, args.mappings)
            if args.report:
                args.report.parent.mkdir(parents=True, exist_ok=True)
                args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(f"Nabu failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    if result.get("rejected", 0):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
