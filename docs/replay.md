# Historical plan reconstruction

The first example reconstructs **XD-238 at the end of 17 June 2013 (UTC)**,
the day it was created. This is an explicit planning cutoff, not a claim about
when development began. Several epics in this dataset have late administrative
status transitions, so first `In Progress` is not automatically a valid start date.

```powershell
python -m nabu replay --database data/nabu.sqlite --epic XD-238 --as-of '2013-06-17T23:59:59.999999Z' --output data/replays/xd-238-first-day
```

Use a new output directory for each run; existing output files are protected.
The cutoff is inclusive. Offset-aware timestamps are converted to UTC;
timezone-naive inputs use TAWOS's UTC convention.

## Separate model input from evaluation evidence

| File | Purpose |
| --- | --- |
| `plan.json` | Historical field values and observed scope; the only artifact intended as review-agent input |
| `audit.json` | Reconstruction evidence, including references to later logs; marked `not_model_input` |
| `outcome.json` | Later outcomes and scope additions; marked `evaluation_only` |

The verified local example is in `data/replays/xd-238-first-day-verified/`.
Those artifacts, like the source dataset, are ignored by Git. The reader opens
SQLite in read-only mode and holds one consistent read transaction.

For each allowlisted field (title, description, type, status and planned points),
the reader finds the last change at/before the cutoff and the first change after
it. The earlier change's new value and the later change's old value describe the
interval containing the cutoff. If both are available they must agree; same-time
ambiguities and disagreements become unknown. A later event's **new** value is
never used to reconstruct that earlier interval.

Using an old value from a later change log is archival reconstruction. It does
not assert that the later event itself was available on the planning day. Such
event timestamps and IDs stay in the audit artifact. The method assumes recorded
old values are accurate and fields persist between logged changes. It cannot
prove that the source history has no missing changes.

When there is no relevant event, a snapshot value is allowed only if its
`updated_at` is at/before the cutoff. Otherwise the field is null **and** listed
in `unknown_fields`. A known empty/null value is not listed as unknown. Display
values missing behind non-null source IDs are not silently treated as empty;
numeric point values can be recovered from their numeric source value.

This deliberately excludes `resolved_at`, resolution, actual points, effort,
duration, latest update time, and outcome-derived flags from the plan. Current
dependency links lack trustworthy creation timestamps and are reported unknown.
Comments are excluded because their creation time does not date later edits to
their current text.

Membership uses only parent `Epic Child` and child `Epic Link` observations at or
before the cutoff. Jira IDs are resolved separately from TAWOS surrogate IDs.
Removals are applied, future-created issues are excluded, and conflicting
same-time membership is withheld. Scope is labelled `observed_membership_only`:
an absence of recorded membership is not proof that a ticket was never planned.
Unresolved references appear in the audit. Source keys and creation dates are
treated as dataset locators; historical key/project migrations are not yet
reconstructed.

## What the real example shows

At the cutoff, the recoverable root title is:

> Provide a strategy in which custom code can be deployed into the DIRT runtime

Its short description says shipped modules should be packaged like contributed
modules. The later title, “Deploying Custom Code”, and its much longer description
are excluded. The observed child tickets are **XD-132** and **XD-194**.

The original root estimate and type have insufficient temporal evidence and
remain unknown. Some child text and estimates are also unknown. This is a useful
**partial reconstruction**, not yet a fully specified plan for forecasting.

The separate reveal records resolution on **21 October 2013**, with resolution
`Complete`. Six additional distinct tickets were observed joining after the
cutoff and before that recorded resolution; seven more were observed joining
after it. Post-resolution reuse must not be presented as original delivery scope.
These observations do not establish a missed deadline: no baseline deadline was
recovered. Counts are distinct additions, not simultaneous scope or net growth.

## Verification

The automated tests cover future-value isolation, unknown versus known-null
values, inclusive cutoffs, timezone conversion, source ID namespaces, membership
removals/conflicts, old snapshot fallback and read-only artifact generation.

A real-data perturbation check ran on a temporary database copy. It changed
3,550 later snapshots, replaced 12,287 later event new-values, removed all 940
current link records, and inserted a later membership addition. **The historical
plan was identical**, while the original database remained unchanged. Results
are saved in `data/replays/xd-238-first-day-verified/verification.json` and the
one-off script in `data/verify_xd_replay.py`.

That check holds historical old-value anchors and source identities fixed. It
tests separation from later values, not source-history completeness or the
accuracy of every recovered field. Before forecasting, improve field coverage
or select an epic whose original plan is more fully evidenced, then construct a
separate cutoff-bound historical comparison corpus.
