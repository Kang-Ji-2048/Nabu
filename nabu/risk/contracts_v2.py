"""Immutable v2 assessment and report contracts, separate from the v1 runtime.

These checks establish structure, provenance bindings and review completion.
They do not establish factual support, calibrate a model, execute company policy,
or verify the meaning of generated report prose.
"""

import hashlib
import json
import math
from collections.abc import Mapping
from typing import Annotated, Any, Literal

from pydantic import AfterValidator, AwareDatetime, ConfigDict, Field, field_validator, model_validator

from ..agents.contracts import StrictModel


def _nonblank(value: str) -> str:
    if not value.strip():
        raise ValueError("Value must contain non-whitespace text")
    return value


NonBlank = Annotated[str, Field(strict=True, min_length=1), AfterValidator(_nonblank)]
Sha256 = Annotated[str, Field(strict=True, pattern=r"^[a-f0-9]{64}$")]
ReviewDecision = Literal["pass", "revise", "needs_review"]
ReviewCheck = Literal[
    "schema", "evidence", "support", "counterexamples", "solution",
    "confidence", "policy", "report_fidelity", "coverage",
]
RISK_REVIEW_CHECKS = frozenset({
    "schema", "evidence", "support", "counterexamples", "solution",
    "confidence", "policy", "coverage",
})


class FrozenContract(StrictModel):
    model_config = ConfigDict(extra="forbid", frozen=True, revalidate_instances="always")


class FrozenCitation(FrozenContract):
    item_id: NonBlank
    field: Literal["title", "description"]
    quote: NonBlank = Field(max_length=500)


class ConfidenceAssessment(FrozenContract):
    target: Literal["warning_supported"]
    status: Literal["uncalibrated", "calibrated", "unknown"]
    evidence_strength: Literal["weak", "moderate", "strong", "unknown"]
    rationale: NonBlank
    score: Annotated[float, Field(ge=0, le=1, allow_inf_nan=False)] | None
    calibrator_id: NonBlank | None
    calibrator_version: NonBlank | None

    @field_validator("score", mode="before")
    @classmethod
    def real_score(cls, value):
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Confidence score must be a finite real number or null")
        if not 0 <= value <= 1:
            raise ValueError("Confidence score must be between 0 and 1")
        if not math.isfinite(value):
            raise ValueError("Confidence score must be finite")
        return value

    @model_validator(mode="after")
    def calibration_status(self):
        calibration = (self.score, self.calibrator_id, self.calibrator_version)
        if self.status == "calibrated":
            if any(value is None for value in calibration):
                raise ValueError("Calibrated confidence requires a score and calibrator identity/version")
        elif any(value is not None for value in calibration):
            raise ValueError("Uncalibrated or unknown confidence must not carry a score or calibrator")
        if self.status == "unknown" and self.evidence_strength != "unknown":
            raise ValueError("Unknown confidence requires unknown evidence strength")
        return self


class PolicyRule(FrozenContract):
    rule_id: NonBlank
    level: NonBlank
    criteria: tuple[NonBlank, ...] = Field(min_length=1)


class CompanyRiskPolicy(FrozenContract):
    schema_version: Literal["nabu-risk-policy-v1"]
    company_id: NonBlank
    policy_id: NonBlank
    policy_version: NonBlank
    levels: tuple[NonBlank, ...] = Field(min_length=1, max_length=10)
    rules: tuple[PolicyRule, ...] = Field(min_length=1, max_length=100)

    @model_validator(mode="after")
    def consistent_rules(self):
        if len(set(self.levels)) != len(self.levels):
            raise ValueError("Policy levels must be unique")
        if len({rule.rule_id for rule in self.rules}) != len(self.rules):
            raise ValueError("Policy rule IDs must be unique")
        if any(rule.level not in self.levels for rule in self.rules):
            raise ValueError("Every rule must reference a declared policy level")
        return self


class PolicyDecision(FrozenContract):
    status: Literal["assigned", "unknown"]
    level: NonBlank | None
    rule_id: NonBlank | None
    rationale: NonBlank
    missing_inputs: tuple[NonBlank, ...]

    @model_validator(mode="after")
    def assignment_status(self):
        if self.status == "assigned":
            if self.level is None or self.rule_id is None or self.missing_inputs:
                raise ValueError("Assigned risk level requires a level/rule and no missing inputs")
        elif self.level is not None or self.rule_id is not None or not self.missing_inputs:
            raise ValueError("Unknown risk level requires null level/rule and explicit missing inputs")
        return self


class AssessedRisk(FrozenContract):
    id: NonBlank = Field(max_length=80)
    risk_type: NonBlank = Field(max_length=100)
    claim: NonBlank = Field(max_length=1500)
    rationale: NonBlank = Field(max_length=3000)
    suggested_action: NonBlank = Field(max_length=1500)
    target_item_ids: tuple[NonBlank, ...] = Field(min_length=1, max_length=10)
    citations: tuple[FrozenCitation, ...] = Field(min_length=2, max_length=10)
    confidence: ConfidenceAssessment
    risk_level: PolicyDecision

    @model_validator(mode="after")
    def distinct_references(self):
        if len(set(self.target_item_ids)) != len(self.target_item_ids):
            raise ValueError("Target item IDs must be unique")
        if len({citation.item_id for citation in self.citations}) < 2:
            raise ValueError("At least two distinct cited ticket IDs are required")
        return self


class AssessmentBundle(FrozenContract):
    schema_version: Literal["nabu-assessment-v2"]
    assessment_id: NonBlank
    plan_id: NonBlank
    as_of: AwareDatetime
    evidence_fingerprint: Sha256
    model_input_fingerprint: Sha256
    model_provider: Literal["local", "anthropic"]
    model_id: NonBlank
    model_artifact_sha256: Sha256 | None
    prompt_version: NonBlank
    policy: CompanyRiskPolicy
    risks: tuple[AssessedRisk, ...] = Field(max_length=8)
    limitations: tuple[NonBlank, ...] = Field(max_length=12)

    @model_validator(mode="after")
    def risk_identity_and_policy(self):
        if self.model_provider == "local" and self.model_artifact_sha256 is None:
            raise ValueError("A local detector requires its model artifact hash")
        if self.model_provider == "anthropic" and self.model_artifact_sha256 is not None:
            raise ValueError("Hosted Claude weights are unavailable; model artifact hash must be null")
        if len({risk.id for risk in self.risks}) != len(self.risks):
            raise ValueError("Risk IDs must be unique")
        rules = {rule.rule_id: rule for rule in self.policy.rules}
        for risk in self.risks:
            decision = risk.risk_level
            if decision.status == "assigned":
                rule = rules.get(decision.rule_id)
                if rule is None or decision.level != rule.level:
                    raise ValueError("Assigned risk level must match its declared company policy rule")
        return self


class ManagerFinding(FrozenContract):
    check: ReviewCheck
    risk_id: NonBlank | None
    decision: ReviewDecision
    reason: NonBlank


class ManagerReview(FrozenContract):
    schema_version: Literal["nabu-manager-review-v1"]
    assessment_id: NonBlank
    assessment_fingerprint: Sha256
    presentation_fingerprint: Sha256 | None
    stage: Literal["risk_review", "report_review"]
    decision: ReviewDecision
    findings: tuple[ManagerFinding, ...] = Field(min_length=1, max_length=100)
    reviewer_id: NonBlank
    reviewer_version: NonBlank
    round: Annotated[int, Field(strict=True, ge=1, le=2)]

    @model_validator(mode="after")
    def aggregate_decision(self):
        if self.stage == "risk_review" and self.presentation_fingerprint is not None:
            raise ValueError("Risk review must not reference a presentation")
        if self.stage == "report_review" and self.presentation_fingerprint is None:
            raise ValueError("Report review requires a presentation fingerprint")
        priority = {"pass": 0, "revise": 1, "needs_review": 2}
        worst = max((finding.decision for finding in self.findings), key=priority.__getitem__)
        if self.decision != worst:
            raise ValueError("Manager decision must match the most restrictive finding decision")
        return self


def assessment_fingerprint(bundle: AssessmentBundle | Mapping[str, Any]) -> str:
    """Hash validated canonical content; review and report fields are excluded."""
    validated = AssessmentBundle.model_validate(bundle)
    canonical = json.dumps(
        validated.model_dump(mode="json"), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


class ReportHandoff(FrozenContract):
    schema_version: Literal["nabu-report-handoff-v2"]
    assessment: AssessmentBundle
    assessment_fingerprint: Sha256
    manager_review: ManagerReview

    @model_validator(mode="after")
    def reviewed_assessment(self):
        fingerprint = assessment_fingerprint(self.assessment)
        if self.assessment_fingerprint != fingerprint:
            raise ValueError("Handoff fingerprint does not match the assessment content")
        review = self.manager_review
        if review.assessment_id != self.assessment.assessment_id or review.assessment_fingerprint != fingerprint:
            raise ValueError("Manager review must reference this exact assessment")
        if review.stage != "risk_review" or review.decision != "pass":
            raise ValueError("Report handoff requires a passed risk review")
        risk_ids = {risk.id for risk in self.assessment.risks}
        if any(finding.risk_id is not None and finding.risk_id not in risk_ids for finding in review.findings):
            raise ValueError("Manager review references an unknown risk ID")
        if not risk_ids:
            if not any(finding.risk_id is None and finding.check == "coverage" and finding.decision == "pass"
                       for finding in review.findings):
                raise ValueError("An empty assessment requires a passed overall coverage check")
        for risk_id in risk_ids:
            passed = {finding.check for finding in review.findings
                      if finding.risk_id == risk_id and finding.decision == "pass"}
            if not RISK_REVIEW_CHECKS <= passed:
                raise ValueError("Every risk requires all risk-review checks to pass")
        return self


class ReportSectionV2(FrozenContract):
    risk_id: NonBlank
    title: NonBlank = Field(max_length=200)
    explanation: NonBlank = Field(max_length=2000)


class PresentationV2(FrozenContract):
    schema_version: Literal["nabu-presentation-v2"]
    assessment_id: NonBlank
    assessment_fingerprint: Sha256
    sections: tuple[ReportSectionV2, ...] = Field(max_length=8)

    @model_validator(mode="after")
    def unique_sections(self):
        if len({section.risk_id for section in self.sections}) != len(self.sections):
            raise ValueError("Report section risk IDs must be unique")
        return self


def presentation_fingerprint(presentation: PresentationV2 | Mapping[str, Any]) -> str:
    """Bind review to the exact validated report wording and assessment reference."""
    validated = PresentationV2.model_validate(presentation)
    canonical = json.dumps(
        validated.model_dump(mode="json"), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def validate_presentation_v2(raw: Any, handoff: ReportHandoff | Mapping[str, Any]) -> PresentationV2:
    """Check identity and risk coverage; generated prose still needs review."""
    checked_handoff = ReportHandoff.model_validate(handoff)
    presentation = PresentationV2.model_validate(raw)
    assessment = checked_handoff.assessment
    if (presentation.assessment_id != assessment.assessment_id or
            presentation.assessment_fingerprint != assessment_fingerprint(assessment)):
        raise ValueError("Presentation must reference the exact reviewed assessment")
    if {section.risk_id for section in presentation.sections} != {risk.id for risk in assessment.risks}:
        raise ValueError("Presentation must include every reviewed risk exactly once")
    return presentation


class ReviewedReport(FrozenContract):
    schema_version: Literal["nabu-reviewed-report-v2"]
    handoff: ReportHandoff
    presentation: PresentationV2
    manager_review: ManagerReview

    @model_validator(mode="after")
    def reviewed_presentation(self):
        presentation = validate_presentation_v2(self.presentation, self.handoff)
        assessment = self.handoff.assessment
        review = self.manager_review
        if review.stage != "report_review" or review.decision != "pass":
            raise ValueError("Reviewed report requires a passed report review")
        if (review.assessment_id != assessment.assessment_id or
                review.assessment_fingerprint != assessment_fingerprint(assessment)):
            raise ValueError("Report review must reference this exact assessment")
        if review.presentation_fingerprint != presentation_fingerprint(presentation):
            raise ValueError("Report review must reference this exact presentation")
        risk_ids = {risk.id for risk in assessment.risks}
        if any(finding.risk_id is not None and finding.risk_id not in risk_ids for finding in review.findings):
            raise ValueError("Report review references an unknown risk ID")
        if not risk_ids:
            if not any(finding.risk_id is None and finding.check == "coverage" and finding.decision == "pass"
                       for finding in review.findings):
                raise ValueError("An empty report requires a passed overall coverage check")
        for risk_id in risk_ids:
            if not any(finding.risk_id == risk_id and finding.check == "report_fidelity" and finding.decision == "pass"
                       for finding in review.findings):
                raise ValueError("Every reported risk requires a passed report-fidelity check")
        return self
