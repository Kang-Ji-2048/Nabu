# Build plan

## Pitch

Teams repeat the same delivery mistakes because the lessons are buried in old tickets. Nabu reads a team's past work in any tracker and reviews each new plan before work starts.

- **Customer:** delivery leads, engineering managers and PMOs at scale-ups (roughly 50 to 500 engineers), plus consultancies that run delivery for clients.
- **Problem:** optimistic estimates, missed dependencies and forgotten work (migrations, QA, docs) cause slips that the team's own history could have predicted.
- **Product in one line:** a team of agents that turns ticket history into cited warnings, missing tickets and a realistic date range on every new epic.
- **Why platform-agnostic:** most organisations mix trackers. A normalisation layer means one product, and lessons learned across all of them.
- **Closest alternatives:** LinearB and Jellyfish show delivery metrics after the fact; Atlassian Rovo is tied to Atlassian. None we know of critiques a plan before work starts (not verified in depth).

## Architecture

Two halves share one store. Adapters normalise every tracker into the canonical schema and the historian learns patterns from it offline. Each new plan then goes through the agent team, which reads only the canonical store, never a platform directly.

```
Jira / Linear / GitHub Issues / Azure DevOps
        -> Adapters (one mapping per source)
        -> Canonical store (work_item, link, event + embeddings)
        -> Historian (clusters history into cited failure patterns)

New epic or plan -> Planner -> [Estimator | Dependency hunter | Gap finder]
                 -> Critic (2+ cited tickets; weak warnings go back once)
                 -> Writer -> Risk review
```

Adding a platform means writing one adapter and one mapping file; nothing downstream of the store changes.

## Canonical schema

| Table | Field | Type | Notes |
| --- | --- | --- | --- |
| work_item | id, source, source_key | text | source = jira, linear, github, ado |
| work_item | type | enum | epic, story, task, bug |
| work_item | title, description | text | description is the main NLP input |
| work_item | parent_id | text | links a story to its epic |
| work_item | team, assignee, labels, components | text / text[] | components drive the pattern matching |
| work_item | estimate, estimate_unit | number, enum | points or hours; normalise per team |
| work_item | created_at, started_at, resolved_at, due_at | timestamp | actual duration = resolved minus started |
| work_item | status_category | enum | todo, in_progress, done, cancelled |
| work_item | raw | json | the original record, untouched |
| link | from_id, to_id, kind | text, enum | blocks, duplicates, relates, causes |
| event | item_id, at, kind, from_value, to_value | mixed | status changes, re-estimates, scope added, reopened |

The event table is what makes delivery mistakes visible: re-estimates, reopens and items added to an epic after it started are all events.

Each source gets a small hand-written mapping file (status names to status_category, link names to link kind). An LLM can draft the mapping for a new platform and a person approves it once.

## Agent team

| Agent | Job | Reads | Hands to |
| --- | --- | --- | --- |
| Historian | Runs offline. Clusters past items and events into named patterns with ticket ids as evidence | All three tables | Pattern store |
| Planner | Splits a new epic into items to check and routes them | The new plan | Specialists |
| Estimator | Finds similar finished items by embedding, compares estimate vs actual | Plan + similar items | Critic |
| Dependency hunter | Finds what similar past work was blocked by and whether the plan has it | link table + patterns | Critic |
| Gap finder | Finds ticket types similar past epics needed but this plan lacks | Sibling items of similar epics | Critic |
| Critic | Drops any warning without at least 2 cited past items; sends weak ones back once | All warnings | Writer |
| Writer | Produces the risk review: warnings, missing tickets, P50/P90 date range | Approved warnings | Output |

**Error recovery:** the critic's send-back loop, retries on malformed specialist output, and adapters that skip and log records they can't map rather than crashing.

**Stack (default):** Python, Claude via the Anthropic API / Agent SDK, Postgres + pgvector on Supabase, a thin web page for the review and live agent log.

## Demo data and script

The demo is a backtest: replay a real past epic, give the agents only what was known on its first day, then reveal what happened.

- **Primary data:** [TAWOS](https://arxiv.org/abs/2202.00979), public agile open-source projects from Jira with story points, links and history.
- **Second adapter:** GitHub Issues from one public repo, or a hand-made Linear CSV, to prove the normalisation layer.
- **Fallback:** the Apache Software Foundation's public Jira via its REST API.

1. Show two trackers' raw records side by side, then the same items in the canonical schema.
2. Pick a past epic that slipped. Hide everything after its start date.
3. Run the review with the agent log streaming.
4. Show the risk review: cited warnings, missing tickets, P50/P90 range.
5. Reveal what actually happened and score the predictions.
6. Close on the business case.

Record one full run before 15:00 as a backup.

## Team split and timeline

| Role | Owns | Done by 12:00 |
| --- | --- | --- |
| Data | Adapters, schema, loading TAWOS and the second source | Both sources loaded |
| Agents | Historian, specialists, critic, writer | One epic reviewed end to end |
| Interface | Review page, live agent log, backtest reveal | Page shows a stored review |
| Pitch | Customer story, slides, demo epic, recording | Demo epic chosen and outcome written down |

1. 09:00-09:30: agree the schema and each agent's JSON output.
2. 12:00: full rough run on one epic.
3. 13:30: feature freeze.
4. 14:30: record the backup run.
5. 15:00: submit.

## Risks

- **Estimates aren't comparable across teams:** compare each item to its own team's history, or use durations.
- **Thin history in public data:** pick the demo project for data richness.
- **Noisy warnings:** the critic's evidence rule matters more than any prompt.
- **Backtest leakage:** filter by date in the query, not the prompt.
- **Clean build:** only public data and code written on the day.

## Tonight

- [ ] Download TAWOS and load one project into Postgres
- [ ] Pick 2-3 candidate epics that slipped and note what happened
- [ ] Set up the repo, Supabase project and API keys
- [ ] Write the schema and agent output contracts as code
