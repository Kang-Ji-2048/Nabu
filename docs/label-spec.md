# Spring XD annotation specification v2

The annotation unit is a ticket at a historical cutoff, with any recoverable
acceptance criteria and observed epic root/sibling context. Labels are multi-label.
Unknown or contradictory evidence requires abstention. Topics and ticket types
alone are insufficient.

| Target definition | Meaning | Source |
| --- | --- | --- |
| `explicit_unresolved_delivery_concern_at_cutoff` | Historical text explicitly supports an unresolved concern affecting this ticket | Evidence-backed Laya/Jev/Claude judgement |
| `later_recorded_outcome_proxy` | A qualifying event occurs in the declared later observation window | Deterministic history rule |

These targets stay separate. An estimate increase does not establish that earlier
text expressed estimation uncertainty. A dependency concern can exist without a
future blocker status. Outcome proxies never vote in teacher consensus.

| Type | Positive | Negative | Insufficient |
| --- | --- | --- | --- |
| `scope_gap` | Explicit necessary requirement or acceptance criterion remains uncovered | Explicit coverage or inapplicability of that particular requirement | Missing criteria history, short text or absence from partial epic membership |
| `dependency` | Explicit unresolved prerequisite/blocker affects delivery | Explicit resolution, availability or inapplicability of that prerequisite | Integration topic or current snapshot link alone |
| `estimation` | Explicit unresolved effort/complexity/estimate uncertainty threatens delivery | Explicit resolution of that specific uncertainty | Zero/unknown points, large estimate or difficult topic alone |
| `rework` | Explicit defect, failed approach or unresolved quality concern threatens repeated work | Explicit resolution/inapplicability of that concern | Bug type, ordinary PR review, planned tests or open work alone |

Every accepted positive and negative needs an exact excerpt in known supplied
text, with ticket ID, field and offset. A root/sibling excerpt must apply to the
target ticket. Substring checks verify provenance; evaluation checks correctness.

## TAWOS Spring XD evidence

The current import has 3,707 work items, 43,227 changes, 109 snapshot epics,
610 `Story Points` events, 541 `Actual Story Points` events, 141 `Acceptance Criteria`
events and 4,242 combined `Epic Child`/`Epic Link` events.

Recorded status destinations are `To Do`, `In Progress`, `In PR`, and `Done`.
There are 130 `Done` to `In Progress` transitions across all history. `In PR` is an
ordinary review stage. No blocked-status transitions exist in XD; dependency
annotation therefore needs explicit historical text until reliable temporal links
are implemented.

Estimate-increase proxies require a finite positive old estimate. Zero-to-positive
transitions are excluded as possible initial sizing/defaults. Actual points,
time spent, rank, sprint moves and fix-version moves do not independently label
delivery risk. No-signal outcome targets remain null, never safe negatives.

Acceptance criteria use adjacent change-log values; no later snapshot is substituted
for missing history. Epic membership is observed and may be incomplete. Current
links have no reliable relationship-creation timestamps: they are excluded from
features and used only to group related tickets conservatively during splitting.
Comments are excluded because creation time does not establish when current text
was last edited.

## Quality policy

Independent reviewed references measure per-type precision/recall and support
threshold selection. Multiple runs of the same served model do not count as
independent sources. Distinct models can share errors, so consensus stays weak.

Chronological splits respect observation-window ends and group repeated tickets,
observed epic members, snapshot-related tickets, exact normalized text and matching
long titles. Groups are reserved for their latest partition; earlier rows and
boundary-crossing outcome windows are quarantined. Semantic near duplicates beyond
those text checks remain a limitation.

All automatic exports are unvalidated weak supervision until independent quality
has been measured. Bulk labelling remains automatic; evaluation references are
never fabricated from teacher predictions.
