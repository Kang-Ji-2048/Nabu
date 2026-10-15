# Confidence, company policy and report handoff schemas

The v2 contracts describe the data needed to carry an evidence-grounded risk
assessment through company-specific grading, manager review and report writing.
They are opt-in schemas in `nabu/risk/contracts_v2.py`. They do not add a trained
model, confidence calibration, a company rules engine or a manager agent. The
current `assess` runtime, v1 `Detection` contract and adapter training remain
unchanged.

## Keep three judgements separate

- **Evidence strength** describes the support for the warning in the supplied
  historical evidence.
- **Confidence** concerns the target `warning_supported`: whether the warning is
  supported. A calibrated score is not a prediction of the probability that the
  project will fail or be delayed.
- **Risk level** is the result of a particular company's versioned policy. It
  can depend on impact, exposure and other inputs that the supplied tickets do
  not establish.

A plausible warning can therefore have strong historical support while its
company risk level remains unknown. A missing calibration or policy input must
remain visible rather than becoming an invented number or level.

## Contract boundaries

| Contract | Purpose |
| --- | --- |
| `ConfidenceAssessment` | Evidence strength, calibration status and the declared confidence target |
| `CompanyRiskPolicy` | Company identity, policy version, custom level names and rules |
| `PolicyDecision` | A level and the rule assigning it, or an unknown decision with missing inputs |
| `AssessedRisk` | Claim, rationale, action, targets and citations, plus separate confidence and policy decisions |
| `AssessmentBundle` | Risks and limitations bound to a plan, historical cutoff, model, artifact, input, prompt and policy provenance |
| `ManagerReview` | Per-risk checks, findings, aggregate decision, reviewer identity/version and review round |
| `ReportHandoff` | A fingerprinted assessment with a complete, passed risk review |
| `PresentationV2` | Report sections tied to the same assessment ID and fingerprint |
| `ReviewedReport` | A handoff and presentation bound to a passed review of that exact report |

`AssessedRisk` has no generic `severity` field. Company levels belong to the
policy decision, so changing a company's policy does not change what the cited
historical text says.

An assessment records `plan_id`, a timezone-aware `as_of`, and
`model_input_fingerprint` in addition to `evidence_fingerprint`. Binding the
complete model input matters because the plan can change while its prior-work
evidence remains the same. These fields identify the supplied assessment
context; they do not independently verify the source data.

`model_provider` identifies the detector as `local` or `anthropic`. A local
detector requires `model_artifact_sha256`. For hosted Claude this field must be
null: a configuration or response hash must not be represented as a weights
hash. Record the actual detector model ID and its prompt version. These fields
describe the detector; a future multi-agent runtime must separately log each
role's provider, model, prompt version and calls. The current manager records
also identify their reviewer and reviewer version.

## Confidence and company levels

`ConfidenceAssessment.status` is `uncalibrated`, `calibrated` or `unknown`. Its
target is `warning_supported`. A numerical score and a calibrator identity and
version are permitted only for `calibrated` assessments, and all are required in
that state. For `uncalibrated` and `unknown`, `score`, `calibrator_id` and
`calibrator_version` must be null. An unknown assessment must also have unknown
evidence strength. An SLM's self-reported certainty is not evidence of calibration.
The named calibrator and its evaluation still need to be established outside
the schema, using appropriate labelled evaluation data for the deployed model.

The policy contract supports custom level names instead of assuming that every
company uses `low`, `medium` and `high`. An assigned level must identify the
applicable policy and rule. If a decision cannot be made because required inputs
are absent, record an unknown decision and those missing inputs. Declaring a
policy and recording a decision do not demonstrate that its rules were executed
correctly; an implementation and review must establish that.

Do not convert v1 `severity` into a company level automatically. Do not infer a
confidence score from severity, citation count or a model's wording.

## Manager review and bounded revision

Reviews distinguish `risk_review` from `report_review`. The review records
checks and findings for each risk, an aggregate `pass`, `revise` or
`needs_review` decision, the reviewer identity/version, and round 1 or 2. This
makes revision requests explicit and bounds the review record to two rounds;
it does not implement an agent loop. The aggregate decision must match the most
restrictive finding: `needs_review`, then `revise`, then `pass`.

A risk review has a null `presentation_fingerprint`. A report review requires a
non-null presentation fingerprint so its decision refers to particular report
content, rather than just an assessment.

Risk review needs to examine the proposed claim against all supplied evidence,
including counterexamples, contradictions and work already included in the
plan. Exact quotes alone do not establish that the historical mechanism applies
to the planned change. Report review needs to check that the prose preserves
the accepted assessment. A reviewer identity can identify a software reviewer;
the field is not proof of human approval.

`ReportHandoff` requires a complete, passed risk review for the same assessment.
The Python validators check the relevant risk coverage and review decisions.
Each risk needs passed `schema`, `evidence`, `support`, `counterexamples`,
`solution`, `confidence`, `policy` and `coverage` findings. An empty assessment
still needs a passed overall coverage finding.

If a revision changes the assessment, create a matching fingerprint and review
that version before handing it to the reporter. An old pass must not authorize
changed claims, actions, confidence or company levels.

## Claude's reporting boundary

The handoff binds an assessment ID and fingerprint to its content. Each
`PresentationV2` section can contain only `risk_id`, `title` and `explanation`.
The presentation also identifies the assessment and its fingerprint. Its
standalone contract rejects duplicate section IDs; use
`validate_presentation_v2(raw, handoff)` to require exactly one section per
reviewed risk and the matching assessment ID and fingerprint. A presentation
cannot add structured risk levels, confidence scores, actions or citations.

`presentation_fingerprint(presentation)` fingerprints the validated report
content. `ReviewedReport` binds the handoff, presentation and a passed
`report_review` to the same assessment and that exact presentation fingerprint.
It requires passed `report_fidelity` findings for each risk. Changing a report's
title or explanation changes its fingerprint and requires a new report review;
the previous pass must not be reused for edited prose.
An empty report still requires a passed overall coverage finding.

Future runtime wiring should render substantive facts, including the accepted
action, directly from the immutable assessment bundle. Claude supplies the
report prose. The structural boundary cannot stop an explanation from making
an unsupported assertion in natural language, so semantic report review is
still required. These contracts do not change the current v1 reporter.

## Export and validate

The [checked-in workflow schema](schemas/risk-workflow-v2.schema.json) describes
the complete v2 interface. Export a fresh copy without calling a model:

```sh
python -m nabu slm-schema --contract workflow --output data/schema-exports/risk-workflow-v2.schema.json
```

The workflow export is an aggregate schema using `oneOf` for the six v2
top-level contracts. Individual exports are available with
`--contract assessment`, `company-policy`, `manager-review`, `report-handoff`, `presentation`
or `reviewed-report`. `--contract detection` remains the default and exports the
existing v1 detector schema:

```sh
python -m nabu slm-schema --contract detection --output data/schema-exports/detection-v1.schema.json
```

The exporter refuses to overwrite an existing output; choose a new path when
comparing versions.

JSON Schema checks the exported shapes and field constraints. Use the Python
contracts and their validators as well for conditional status requirements,
assessment and presentation fingerprints, policy references, complete risk
coverage and agreement between a handoff and its presentation. A JSON Schema
consumer alone cannot establish these relationships.

Validate the original v1 detector candidate against the frozen input with
`validate_detection` before augmenting it into v2. `AssessedRisk` has no
`severity` field and must not be passed directly to that v1 validator. Adopting
v2 does not replace evidence validation.

Schema-valid text does not prove exact evidence matches or semantic support.
Neither validation route proves calibration quality or that free-form prose is
safe and accurate.

## Migration from v1

1. Keep existing detector outputs and supervised targets in the v1
   `{ "risks": [...], "limitations": [...] }` shape. Existing label validation
   and training workflows continue to use `Detection`.
2. Introduce v2 as a separate assessment layer, preserving the detector's input
   and artifact provenance. Supply an explicit company policy and record
   missing decision inputs.
3. Record confidence as uncalibrated or unknown until an appropriate calibrator
   has been fitted and evaluated. Existing v1 outputs have no automatic
   confidence value.
4. Validate and review the resulting assessment before creating a report
   handoff. Wire deterministic rendering, report review and any revision loop
   separately before using these contracts in live assessment.

The schema export is a reviewable interface for that work. It is not a claim
that these capabilities are already trained, evaluated or running in `assess`.
