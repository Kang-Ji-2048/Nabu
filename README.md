# Nabu: Delivery Risk Reviewer

## Local Laya risk labelling

The [Laya setup guide](docs/laya.md) runs ticket risk labelling locally on Windows,
Linux or Apple Silicon, with a pinned downloadable checkpoint, evidence checks,
resumable batches and training exports. See the [Spring XD label specification](docs/label-spec.md)
and [labelling workflow](docs/labelling.md). SLM training remains separate.
The current zero-shot Laya checkpoint is experimental: the first five XD tickets
all abstained at confidence 0.8, so it is not yet a validated dataset labeller.

## SLM-to-Claude architecture

The new flow is **ingest → normalise and classify → SQLite → local SLM risk
detection → citation validation → Claude reporting → Markdown/JSON review**.
Run it with `python -m nabu assess`; `review` remains the legacy investigator
baseline. See [the architecture overview](docs/architecture.md) and
[the SLM setup and training handoff](docs/slm.md).

The integration includes an AI-reviewed experimental XD dataset and frozen
Mesos test references. See [the M4 Pro 48GB training handoff](docs/training-handoff.md)
for preparation and the separate training command. Live assessment still
requires a trained model and provenance manifest. Offline mode is a wiring test,
not a risk assessment.

Nabu reads a team's ticket history from any tracker and warns them, before work starts, where a new plan is likely to go wrong.

- **In:** past tickets from Jira, Linear, GitHub Issues or Azure DevOps, normalised into one schema, plus a new epic or sprint plan.
- **Agents:** a historian learns the team's failure patterns; an estimator, a dependency hunter and a gap finder check the new plan; a critic keeps only warnings backed by cited past tickets; a writer produces the review.
- **Out:** a risk review with cited warnings, suggested missing tickets and a realistic P50/P90 date range.
- **Demo:** a backtest on a real public project. The agents review a past epic using only what was known on day one, then we reveal what actually happened.

Built for the Accel AI Innovate London hackathon (15 Oct 2026), challenge "Long Running Agents: From Task to Workflow".

The current build implements TAWOS ingestion, conservative historical replay,
local work-category discovery, semantic retrieval and a LangGraph gap investigator
with citation validation and a critic. The broader agent team and P50/P90
forecasting above describe the intended product roadmap.

See [plan.md](plan.md) for the full build plan.

## ETL pipeline

The first implementation exports one project from a TAWOS SQL dump or MySQL server, preserves its source records and normalizes tickets, change events and links into a local SQLite database.

```powershell
python -m nabu load --input tests/fixtures/tawos-synthetic.jsonl --database data/nabu.sqlite --report data/reports/synthetic.json
```

This command uses synthetic test data. See [docs/etl.md](docs/etl.md) for real-data download, MySQL extraction, mapping, quality reports and historical backtest limitations.

## Historical replay

The replay reader reconstructs an evidence-backed partial plan at a fixed cutoff, with outcomes and audit evidence in separate files. See [docs/replay.md](docs/replay.md) for the real XD-238 example and verification results.

## Agent workflow

LangGraph now runs a tool-driven gap investigator, citation validator and critic, with SQLite checkpoints for recovery. See [docs/agents.md](docs/agents.md) for installation, an offline smoke test, live Anthropic configuration and resumable execution.

## Work categories and semantic retrieval

Local ticket embeddings and HDBSCAN discover proposed work categories without a fixed category count. The investigator can use semantic retrieval against its frozen historical evidence. See [docs/categories.md](docs/categories.md) for model preparation, discovery, search and refresh commands.

Local model training and chronological dataset preparation are described in [docs/slm-training.md](docs/slm-training.md).
