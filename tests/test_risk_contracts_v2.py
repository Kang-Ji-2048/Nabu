"""Synthetic v2 contract checks; no datasets, inference, or training required."""

from copy import deepcopy
import hashlib
import json
import unittest

from pydantic import ValidationError

from nabu.risk.contracts import Detection
from nabu.risk.contracts_v2 import (
    AssessedRisk,
    AssessmentBundle,
    CompanyRiskPolicy,
    ConfidenceAssessment,
    ManagerFinding,
    ManagerReview,
    PolicyDecision,
    PolicyRule,
    PresentationV2,
    ReportHandoff,
    ReportSectionV2,
    ReviewedReport,
    assessment_fingerprint,
    presentation_fingerprint,
    validate_presentation_v2,
)
from nabu.risk.runner import validate_detection


REQUIRED_CHECKS = (
    "schema", "evidence", "support", "counterexamples", "solution",
    "confidence", "policy", "coverage",
)


def confidence_payload(**changes):
    result = {
        "target": "warning_supported",
        "status": "uncalibrated",
        "evidence_strength": "moderate",
        "rationale": "Two historical tickets describe the same explicit constraint.",
        "score": None,
        "calibrator_id": None,
        "calibrator_version": None,
    }
    result.update(changes)
    return result


def policy_payload():
    return {
        "schema_version": "nabu-risk-policy-v1",
        "company_id": "synthetic-company",
        "policy_id": "delivery-policy",
        "policy_version": "2026-10",
        "levels": ["routine", "engineering-review", "executive-review"],
        "rules": [
            {
                "rule_id": "integration-review",
                "level": "engineering-review",
                "criteria": ["A planned integration encounters a documented constraint."],
            },
            {
                "rule_id": "executive-escalation",
                "level": "executive-review",
                "criteria": ["A separately verified company escalation criterion applies."],
            },
        ],
    }


def decision_payload(**changes):
    result = {
        "status": "assigned",
        "level": "engineering-review",
        "rule_id": "integration-review",
        "rationale": "The declared integration review rule applies.",
        "missing_inputs": [],
    }
    result.update(changes)
    return result


def risk_payload(risk_id="risk-1"):
    return {
        "id": risk_id,
        "risk_type": "integration",
        "claim": "The planned integration could encounter the documented protocol constraint.",
        "rationale": "Both prior tickets explicitly identify the same protocol constraint.",
        "suggested_action": "Verify the planned integration against the documented protocol constraint.",
        "target_item_ids": ["PLAN-1"],
        "citations": [
            {"item_id": "PRIOR-1", "field": "title", "quote": "Protocol rejects an empty identifier"},
            {"item_id": "PRIOR-2", "field": "description", "quote": "Identifiers must be populated before submission."},
        ],
        "confidence": confidence_payload(),
        "risk_level": decision_payload(),
    }


def bundle_payload(*, empty=False, two_risks=False):
    risks = [] if empty else [risk_payload()]
    if two_risks:
        risks.append(risk_payload("risk-2"))
    return {
        "schema_version": "nabu-assessment-v2",
        "assessment_id": "synthetic-assessment-1",
        "plan_id": "PLAN-1",
        "as_of": "2020-01-01T00:00:00Z",
        "evidence_fingerprint": "a" * 64,
        "model_input_fingerprint": "d" * 64,
        "model_provider": "local",
        "model_id": "synthetic-detector",
        "model_artifact_sha256": "b" * 64,
        "prompt_version": "synthetic-prompt-v1",
        "policy": policy_payload(),
        "risks": risks,
        "limitations": ["Synthetic evidence used only to exercise contract behavior."],
    }


def finding_payload(check="coverage", risk_id="risk-1", decision="pass"):
    return {
        "check": check,
        "risk_id": risk_id,
        "decision": decision,
        "reason": "Synthetic check result; this fixture is not a human review.",
    }


def review_payload(bundle=None):
    bundle = bundle_payload() if bundle is None else bundle
    findings = [finding_payload(check, risk["id"])
                for risk in bundle["risks"] for check in REQUIRED_CHECKS]
    if not findings:
        findings = [finding_payload("coverage", None)]
    return {
        "schema_version": "nabu-manager-review-v1",
        "assessment_id": bundle["assessment_id"],
        "assessment_fingerprint": assessment_fingerprint(bundle),
        "presentation_fingerprint": None,
        "stage": "risk_review",
        "decision": "pass",
        "findings": findings,
        "reviewer_id": "synthetic-manager",
        "reviewer_version": "fixture-v1",
        "round": 1,
    }


def handoff_payload(bundle=None):
    bundle = bundle_payload() if bundle is None else bundle
    return {
        "schema_version": "nabu-report-handoff-v2",
        "assessment": bundle,
        "assessment_fingerprint": assessment_fingerprint(bundle),
        "manager_review": review_payload(bundle),
    }


def presentation_payload(bundle=None):
    bundle = bundle_payload() if bundle is None else bundle
    return {
        "schema_version": "nabu-presentation-v2",
        "assessment_id": bundle["assessment_id"],
        "assessment_fingerprint": assessment_fingerprint(bundle),
        "sections": [
            {
                "risk_id": risk["id"],
                "title": "Verify the documented integration constraint",
                "explanation": "The assessment identifies a constraint to verify in the planned integration.",
            }
            for risk in bundle["risks"]
        ],
    }


def reviewed_report_payload(bundle=None):
    bundle = bundle_payload() if bundle is None else bundle
    presentation = presentation_payload(bundle)
    review = review_payload(bundle)
    review.update(
        stage="report_review",
        presentation_fingerprint=presentation_fingerprint(presentation),
        findings=([finding_payload("report_fidelity", risk["id"]) for risk in bundle["risks"]]
                  or [finding_payload("coverage", None)]),
    )
    return {
        "schema_version": "nabu-reviewed-report-v2",
        "handoff": handoff_payload(bundle),
        "presentation": presentation,
        "manager_review": review,
    }


class ConfidenceContractTests(unittest.TestCase):
    def test_uncalibrated_keeps_numeric_confidence_and_calibrator_identity_null(self):
        assessment = ConfidenceAssessment.model_validate(confidence_payload())
        self.assertIsNone(assessment.score)
        for field, value in (("score", 0.0), ("score", 0.8),
                             ("calibrator_id", "calibrator"), ("calibrator_version", "v1")):
            with self.subTest(field=field, value=value), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate(confidence_payload(**{field: value}))

    def test_calibrated_score_accepts_endpoints_and_requires_identity_and_version(self):
        valid = confidence_payload(status="calibrated", score=0.75,
                                   calibrator_id="validation-calibrator", calibrator_version="v2")
        for score in (0, 0.4, 1):
            with self.subTest(score=score):
                self.assertEqual(ConfidenceAssessment.model_validate({**valid, "score": score}).score, score)
        for field in ("score", "calibrator_id", "calibrator_version"):
            with self.subTest(missing=field), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate({**valid, field: None})
        for score in (-0.01, 1.01):
            with self.subTest(score=score), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate({**valid, "score": score})

    def test_scores_reject_nonfinite_boolean_and_string_values(self):
        valid = confidence_payload(status="calibrated", score=0.75,
                                   calibrator_id="validation-calibrator", calibrator_version="v2")
        for score in (float("nan"), float("inf"), float("-inf"), True, False, "0.75", "NaN"):
            with self.subTest(score=repr(score)), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate({**valid, "score": score})

    def test_unknown_confidence_requires_unknown_evidence_strength_and_no_calibration(self):
        valid = confidence_payload(status="unknown", evidence_strength="unknown")
        self.assertEqual(ConfidenceAssessment.model_validate(valid).status, "unknown")
        for strength in ("weak", "moderate", "strong"):
            with self.subTest(strength=strength), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate({**valid, "evidence_strength": strength})
        for field, value in (("score", 0.5), ("calibrator_id", "id"), ("calibrator_version", "v1")):
            with self.subTest(field=field), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate({**valid, field: value})

    def test_nullable_confidence_fields_must_be_explicit(self):
        for field in ("score", "calibrator_id", "calibrator_version"):
            raw = confidence_payload()
            del raw[field]
            with self.subTest(field=field), self.assertRaises(ValidationError):
                ConfidenceAssessment.model_validate(raw)


class PolicyAndAssessmentContractTests(unittest.TestCase):
    def test_hosted_claude_provenance_does_not_invent_a_weights_hash(self):
        raw = bundle_payload()
        raw.update(model_provider="anthropic", model_id="synthetic-claude-model",
                   model_artifact_sha256=None)
        bundle = AssessmentBundle.model_validate(raw)
        self.assertIsNone(bundle.model_artifact_sha256)
        ReportHandoff.model_validate(handoff_payload(raw))
        with self.assertRaises(ValidationError):
            AssessmentBundle.model_validate({**raw, "model_artifact_sha256": "b" * 64})

    def test_local_detector_provenance_requires_a_weights_hash(self):
        raw = bundle_payload()
        with self.assertRaises(ValidationError):
            AssessmentBundle.model_validate({**raw, "model_artifact_sha256": None})

    def test_provider_change_invalidates_previous_manager_review(self):
        raw = handoff_payload()
        raw["assessment"].update(model_provider="anthropic", model_artifact_sha256=None)
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate(raw)

    def test_company_can_define_levels_outside_legacy_severity_enum(self):
        policy = CompanyRiskPolicy.model_validate(policy_payload())
        self.assertEqual(policy.levels, ("routine", "engineering-review", "executive-review"))
        self.assertIsInstance(policy.rules[0], PolicyRule)
        self.assertEqual(AssessmentBundle.model_validate(bundle_payload()).risks[0].risk_level.level,
                         "engineering-review")

    def test_policy_rejects_duplicate_levels_duplicate_rules_and_undeclared_rule_level(self):
        duplicate_levels = policy_payload()
        duplicate_levels["levels"].append("routine")
        duplicate_rules = policy_payload()
        duplicate_rules["rules"].append(deepcopy(duplicate_rules["rules"][0]))
        undeclared_level = policy_payload()
        undeclared_level["rules"][0]["level"] = "not-declared"
        for label, raw in (("levels", duplicate_levels), ("rules", duplicate_rules),
                           ("undeclared", undeclared_level)):
            with self.subTest(label=label), self.assertRaises(ValidationError):
                CompanyRiskPolicy.model_validate(raw)

    def test_unknown_decision_requires_missing_inputs_and_null_assignment(self):
        valid = decision_payload(status="unknown", level=None, rule_id=None,
                                 missing_inputs=["Company impact threshold has not been supplied."])
        self.assertEqual(PolicyDecision.model_validate(valid).status, "unknown")
        for changes in ({"missing_inputs": []}, {"level": "routine"}, {"rule_id": "integration-review"}):
            with self.subTest(changes=changes), self.assertRaises(ValidationError):
                PolicyDecision.model_validate({**valid, **changes})

    def test_assigned_decision_requires_level_rule_and_no_missing_inputs(self):
        self.assertEqual(PolicyDecision.model_validate(decision_payload()).status, "assigned")
        for changes in ({"level": None}, {"rule_id": None}, {"missing_inputs": ["Unknown impact"]}):
            with self.subTest(changes=changes), self.assertRaises(ValidationError):
                PolicyDecision.model_validate(decision_payload(**changes))

    def test_nullable_policy_assignment_fields_must_be_explicit(self):
        for field in ("level", "rule_id"):
            raw = decision_payload(status="unknown", level=None, rule_id=None, missing_inputs=["Impact"])
            del raw[field]
            with self.subTest(field=field), self.assertRaises(ValidationError):
                PolicyDecision.model_validate(raw)

    def test_assessed_risk_requires_two_distinct_tickets_and_unique_targets(self):
        self.assertEqual(len(AssessedRisk.model_validate(risk_payload()).citations), 2)
        one_citation = risk_payload()
        one_citation["citations"] = one_citation["citations"][:1]
        same_ticket = risk_payload()
        same_ticket["citations"][1]["item_id"] = "PRIOR-1"
        duplicate_target = risk_payload()
        duplicate_target["target_item_ids"] *= 2
        for label, raw in (("one citation", one_citation), ("two fields on one ticket", same_ticket),
                           ("duplicate target", duplicate_target)):
            with self.subTest(label=label), self.assertRaises(ValidationError):
                AssessedRisk.model_validate(raw)

    def test_bundle_rejects_duplicate_risks_unknown_rules_and_level_rule_mismatch(self):
        duplicate = bundle_payload()
        duplicate["risks"] *= 2
        unknown_rule = bundle_payload()
        unknown_rule["risks"][0]["risk_level"]["rule_id"] = "nonexistent-rule"
        wrong_level = bundle_payload()
        wrong_level["risks"][0]["risk_level"]["level"] = "executive-review"
        for label, raw in (("duplicate risks", duplicate), ("unknown rule", unknown_rule),
                           ("wrong level for rule", wrong_level)):
            with self.subTest(label=label), self.assertRaises(ValidationError):
                AssessmentBundle.model_validate(raw)

    def test_bundle_can_carry_an_explicitly_unknown_company_level(self):
        raw = bundle_payload()
        raw["risks"][0]["risk_level"] = decision_payload(
            status="unknown", level=None, rule_id=None, missing_inputs=["Impact threshold is unknown."])
        bundle = AssessmentBundle.model_validate(raw)
        self.assertIsNone(bundle.risks[0].risk_level.level)
        self.assertIsNone(bundle.risks[0].risk_level.rule_id)

    def test_assessment_requires_cutoff_with_timezone_and_explicit_input_identity(self):
        for as_of in ("2020-01-01T00:00:00", "2020-01-01", "not-a-timestamp"):
            raw = bundle_payload()
            raw["as_of"] = as_of
            with self.subTest(as_of=as_of), self.assertRaises(ValidationError):
                AssessmentBundle.model_validate(raw)
        for field in ("plan_id", "as_of", "model_input_fingerprint"):
            raw = bundle_payload()
            del raw[field]
            with self.subTest(missing=field), self.assertRaises(ValidationError):
                AssessmentBundle.model_validate(raw)
        for fingerprint in ("not-a-hash", "f" * 63, "F" * 64):
            raw = bundle_payload()
            raw["model_input_fingerprint"] = fingerprint
            with self.subTest(fingerprint=fingerprint), self.assertRaises(ValidationError):
                AssessmentBundle.model_validate(raw)

    def test_nested_collections_are_tuples_and_models_are_frozen(self):
        bundle = AssessmentBundle.model_validate(bundle_payload())
        for collection in (bundle.risks, bundle.limitations, bundle.policy.levels, bundle.policy.rules,
                           bundle.policy.rules[0].criteria, bundle.risks[0].target_item_ids,
                           bundle.risks[0].citations, bundle.risks[0].risk_level.missing_inputs):
            with self.subTest(collection=repr(collection)):
                self.assertIsInstance(collection, tuple)
                with self.assertRaises((AttributeError, TypeError)):
                    collection.append("mutation")
        for model, field, value in (
            (bundle, "assessment_id", "mutated"),
            (bundle.policy, "policy_version", "mutated"),
            (bundle.policy.rules[0], "level", "routine"),
            (bundle.risks[0], "claim", "mutated"),
            (bundle.risks[0].citations[0], "quote", "mutated"),
            (bundle.risks[0].confidence, "score", 0.9),
            (bundle.risks[0].risk_level, "level", "routine"),
        ):
            with self.subTest(field=field, model=type(model).__name__), self.assertRaises(ValidationError):
                setattr(model, field, value)

    def test_mutating_source_lists_after_validation_cannot_change_bundle(self):
        raw = bundle_payload()
        bundle = AssessmentBundle.model_validate(raw)
        fingerprint = assessment_fingerprint(bundle)
        raw["risks"][0]["citations"][0]["quote"] = "changed"
        raw["policy"]["rules"][0]["criteria"].append("changed")
        raw["risks"].clear()
        self.assertEqual(assessment_fingerprint(bundle), fingerprint)
        self.assertEqual(len(bundle.risks), 1)


class ManagerAndHandoffContractTests(unittest.TestCase):
    def test_manager_aggregate_decision_matches_most_restrictive_finding(self):
        for decisions, expected in (
            (("pass", "pass"), "pass"),
            (("pass", "revise"), "revise"),
            (("revise", "needs_review", "pass"), "needs_review"),
        ):
            raw = review_payload()
            raw["findings"] = [finding_payload(decision=decision) for decision in decisions]
            raw["decision"] = expected
            with self.subTest(decisions=decisions):
                review = ManagerReview.model_validate(raw)
                self.assertEqual(review.decision, expected)
                self.assertIsInstance(review.findings[0], ManagerFinding)
                for incorrect in {"pass", "revise", "needs_review"} - {expected}:
                    with self.assertRaises(ValidationError):
                        ManagerReview.model_validate({**raw, "decision": incorrect})

    def test_valid_handoff_binds_review_to_assessment(self):
        handoff = ReportHandoff.model_validate(handoff_payload())
        self.assertEqual(handoff.assessment_fingerprint, assessment_fingerprint(handoff.assessment))
        self.assertEqual(handoff.manager_review.assessment_id, handoff.assessment.assessment_id)
        self.assertEqual(handoff.manager_review.decision, "pass")

    def test_handoff_rejects_wrong_content_hash_review_hash_id_and_stage(self):
        for label, update in (
            ("handoff hash", lambda raw: raw.update(assessment_fingerprint="c" * 64)),
            ("review hash", lambda raw: raw["manager_review"].update(assessment_fingerprint="c" * 64)),
            ("assessment ID", lambda raw: raw["manager_review"].update(assessment_id="another-assessment")),
            ("review stage", lambda raw: raw["manager_review"].update(stage="report_review")),
            ("modified content", lambda raw: raw["assessment"]["limitations"].append("New limitation")),
        ):
            raw = handoff_payload()
            update(raw)
            with self.subTest(label=label), self.assertRaises(ValidationError):
                ReportHandoff.model_validate(raw)

    def test_changed_plan_cutoff_or_model_input_invalidates_prior_handoff_and_review(self):
        for field, value in (("plan_id", "PLAN-2"), ("as_of", "2020-01-02T00:00:00Z"),
                             ("model_input_fingerprint", "e" * 64)):
            raw = handoff_payload()
            original_fingerprint = raw["assessment_fingerprint"]
            raw["assessment"][field] = value
            current_fingerprint = assessment_fingerprint(raw["assessment"])
            with self.subTest(field=field):
                self.assertNotEqual(current_fingerprint, original_fingerprint)
                with self.assertRaises(ValidationError):
                    ReportHandoff.model_validate(raw)
                # Updating only the envelope still leaves the old manager review stale.
                raw["assessment_fingerprint"] = current_fingerprint
                with self.assertRaises(ValidationError):
                    ReportHandoff.model_validate(raw)

    def test_handoff_rejects_revise_or_needs_review_even_with_complete_checks(self):
        for decision in ("revise", "needs_review"):
            raw = handoff_payload()
            raw["manager_review"]["decision"] = decision
            raw["manager_review"]["findings"].append(finding_payload("support", decision=decision))
            with self.subTest(decision=decision), self.assertRaises(ValidationError):
                ReportHandoff.model_validate(raw)

    def test_each_risk_requires_every_mandatory_check(self):
        bundle = bundle_payload(two_risks=True)
        ReportHandoff.model_validate(handoff_payload(bundle))
        for risk_id in ("risk-1", "risk-2"):
            for check in REQUIRED_CHECKS:
                raw = handoff_payload(bundle)
                raw["manager_review"]["findings"] = [
                    finding for finding in raw["manager_review"]["findings"]
                    if (finding["risk_id"], finding["check"]) != (risk_id, check)
                ]
                with self.subTest(risk_id=risk_id, missing=check), self.assertRaises(ValidationError):
                    ReportHandoff.model_validate(raw)

    def test_overall_checks_cannot_replace_per_risk_checks(self):
        raw = handoff_payload()
        raw["manager_review"]["findings"] = [finding_payload(check, None) for check in REQUIRED_CHECKS]
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate(raw)

    def test_empty_assessment_requires_a_passed_null_risk_coverage_check(self):
        bundle = bundle_payload(empty=True)
        handoff = ReportHandoff.model_validate(handoff_payload(bundle))
        self.assertEqual(handoff.assessment.risks, ())
        raw = handoff_payload(bundle)
        raw["manager_review"]["findings"] = [finding_payload("schema", None)]
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate(raw)
        raw["manager_review"]["findings"] = [finding_payload("coverage", "risk-1")]
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate(raw)

    def test_unknown_review_risk_ids_are_rejected(self):
        raw = handoff_payload()
        raw["manager_review"]["findings"].append(finding_payload("schema", "unknown-risk"))
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate(raw)

    def test_review_nullable_risk_id_is_explicit_and_round_is_a_strict_bounded_integer(self):
        finding = finding_payload("coverage", None)
        del finding["risk_id"]
        with self.assertRaises(ValidationError):
            ManagerFinding.model_validate(finding)
        for round_number in (True, "1", 0, 3):
            with self.subTest(round=round_number), self.assertRaises(ValidationError):
                ManagerReview.model_validate({**review_payload(), "round": round_number})

    def test_review_stage_controls_explicit_presentation_binding(self):
        raw = review_payload()
        del raw["presentation_fingerprint"]
        with self.assertRaises(ValidationError):
            ManagerReview.model_validate(raw)
        with self.assertRaises(ValidationError):
            ManagerReview.model_validate({**review_payload(), "presentation_fingerprint": "e" * 64})
        with self.assertRaises(ValidationError):
            ManagerReview.model_validate({**review_payload(), "stage": "report_review"})
        report_review = reviewed_report_payload()["manager_review"]
        self.assertEqual(ManagerReview.model_validate(report_review).stage, "report_review")
        raw_handoff = handoff_payload()
        raw_handoff["manager_review"] = report_review
        with self.assertRaisesRegex(ValidationError, "passed risk review"):
            ReportHandoff.model_validate(raw_handoff)

    def test_review_findings_and_handoff_nested_content_are_immutable(self):
        handoff = ReportHandoff.model_validate(handoff_payload())
        self.assertIsInstance(handoff.manager_review.findings, tuple)
        with self.assertRaises(TypeError):
            handoff.manager_review.findings[0] = handoff.manager_review.findings[1]
        with self.assertRaises(ValidationError):
            handoff.manager_review.findings[0].decision = "revise"
        with self.assertRaises(ValidationError):
            handoff.manager_review.round = 2
        with self.assertRaises(ValidationError):
            handoff.assessment.risks[0].suggested_action = "changed"

    def test_unvalidated_model_copy_cannot_bypass_handoff_revalidation(self):
        handoff = ReportHandoff.model_validate(handoff_payload())
        forged_confidence = handoff.assessment.risks[0].confidence.model_copy(update={"score": 0.99})
        forged_risk = handoff.assessment.risks[0].model_copy(update={"confidence": forged_confidence})
        forged_bundle = handoff.assessment.model_copy(update={"risks": (forged_risk,)})
        with self.assertRaises(ValidationError):
            ReportHandoff.model_validate({**handoff_payload(), "assessment": forged_bundle})


class PresentationAndFingerprintContractTests(unittest.TestCase):
    def test_report_sections_expose_only_risk_identity_and_presentation_text(self):
        section = presentation_payload()["sections"][0]
        self.assertEqual(set(ReportSectionV2.model_fields), {"risk_id", "title", "explanation"})
        self.assertEqual(set(ReportSectionV2.model_validate(section).model_dump()),
                         {"risk_id", "title", "explanation"})
        for field, value in (
            ("recommended_action", "Invented action"), ("suggested_action", "Invented action"),
            ("severity", "high"), ("confidence", confidence_payload()),
            ("risk_level", decision_payload()), ("citations", []), ("claim", "New claim"),
        ):
            with self.subTest(field=field), self.assertRaises(ValidationError):
                ReportSectionV2.model_validate({**section, field: value})

    def test_valid_presentation_returns_frozen_model_with_exact_risk_coverage(self):
        bundle = bundle_payload(two_risks=True)
        raw = presentation_payload(bundle)
        raw["sections"].reverse()
        result = validate_presentation_v2(raw, handoff_payload(bundle))
        self.assertIsInstance(result, PresentationV2)
        self.assertEqual({section.risk_id for section in result.sections}, {"risk-1", "risk-2"})
        self.assertIsInstance(result.sections, tuple)
        with self.assertRaises(ValidationError):
            result.sections[0].title = "changed"

    def test_report_must_include_each_risk_exactly_once_without_adding_or_omitting(self):
        bundle = bundle_payload(two_risks=True)
        valid = presentation_payload(bundle)
        omitted = deepcopy(valid)
        omitted["sections"].pop()
        duplicate = deepcopy(valid)
        duplicate["sections"].append(deepcopy(duplicate["sections"][0]))
        invented = deepcopy(valid)
        invented["sections"][0]["risk_id"] = "invented-risk"
        for label, raw in (("omitted", omitted), ("duplicate", duplicate), ("invented", invented)):
            with self.subTest(label=label), self.assertRaises(ValueError):
                validate_presentation_v2(raw, handoff_payload(bundle))

    def test_report_requires_matching_assessment_id_and_hash(self):
        for changes in ({"assessment_id": "another-assessment"}, {"assessment_fingerprint": "c" * 64}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "exact reviewed assessment"):
                validate_presentation_v2({**presentation_payload(), **changes}, handoff_payload())

    def test_stale_report_hash_is_rejected_even_if_current_handoff_is_valid(self):
        stale_presentation = presentation_payload()
        changed = bundle_payload()
        changed["risks"][0]["suggested_action"] = "A revised, structurally valid verification action."
        current_handoff = handoff_payload(changed)
        ReportHandoff.model_validate(current_handoff)
        with self.assertRaisesRegex(ValueError, "exact reviewed assessment"):
            validate_presentation_v2(stale_presentation, current_handoff)

    def test_presentation_validator_revalidates_supplied_handoff(self):
        raw_handoff = handoff_payload()
        raw_handoff["manager_review"]["findings"] = [finding_payload("coverage")]
        with self.assertRaises(ValidationError):
            validate_presentation_v2(presentation_payload(), raw_handoff)

    def test_empty_assessment_has_an_empty_presentation(self):
        bundle = bundle_payload(empty=True)
        result = validate_presentation_v2(presentation_payload(bundle), handoff_payload(bundle))
        self.assertEqual(result.sections, ())
        invented = presentation_payload(bundle)
        invented["sections"] = presentation_payload()["sections"]
        with self.assertRaises(ValueError):
            validate_presentation_v2(invented, handoff_payload(bundle))

    def test_fingerprint_is_deterministic_across_json_roundtrip_and_mapping_key_order(self):
        raw = bundle_payload()
        model = AssessmentBundle.model_validate(raw)

        def reverse_keys(value):
            if isinstance(value, dict):
                return {key: reverse_keys(value[key]) for key in reversed(value)}
            if isinstance(value, list):
                return [reverse_keys(item) for item in value]
            return value

        expected = assessment_fingerprint(model)
        self.assertRegex(expected, r"^[a-f0-9]{64}$")
        self.assertEqual(assessment_fingerprint(raw), expected)
        self.assertEqual(assessment_fingerprint(json.loads(model.model_dump_json())), expected)
        self.assertEqual(assessment_fingerprint(reverse_keys(raw)), expected)
        canonical = json.dumps(model.model_dump(mode="json"), sort_keys=True, separators=(",", ":"),
                               ensure_ascii=False, allow_nan=False).encode("utf-8")
        self.assertEqual(expected, hashlib.sha256(canonical).hexdigest())

    def test_fingerprint_changes_for_assessment_content_and_rejects_invalid_content(self):
        original = bundle_payload()
        changed = deepcopy(original)
        changed["policy"]["policy_version"] = "2026-11"
        self.assertNotEqual(assessment_fingerprint(changed), assessment_fingerprint(original))
        invalid = deepcopy(original)
        invalid["risks"][0]["confidence"]["score"] = 0.8
        with self.assertRaises(ValidationError):
            assessment_fingerprint(invalid)

    def test_presentation_fingerprint_binds_exact_prose_and_is_json_deterministic(self):
        raw = presentation_payload()
        model = PresentationV2.model_validate(raw)
        fingerprint = presentation_fingerprint(model)
        self.assertEqual(presentation_fingerprint(json.loads(model.model_dump_json())), fingerprint)
        reordered = {key: raw[key] for key in reversed(raw)}
        reordered["sections"] = [{key: section[key] for key in reversed(section)}
                                 for section in raw["sections"]]
        self.assertEqual(presentation_fingerprint(reordered), fingerprint)
        changed = deepcopy(raw)
        changed["sections"][0]["explanation"] += " Additional wording."
        self.assertNotEqual(presentation_fingerprint(changed), fingerprint)


class FinalReportGateContractTests(unittest.TestCase):
    def test_reviewed_report_requires_and_accepts_two_separate_passed_reviews(self):
        raw = reviewed_report_payload(bundle_payload(two_risks=True))
        reviewed = ReviewedReport.model_validate(raw)
        self.assertEqual(reviewed.handoff.manager_review.stage, "risk_review")
        self.assertEqual(reviewed.manager_review.stage, "report_review")
        self.assertEqual(reviewed.manager_review.presentation_fingerprint,
                         presentation_fingerprint(reviewed.presentation))
        self.assertEqual(ReviewedReport.model_validate_json(reviewed.model_dump_json()), reviewed)
        with self.assertRaises(ValidationError):
            reviewed.presentation.sections[0].explanation = "changed"

    def test_final_gate_rejects_prose_changed_after_report_review_pass(self):
        for field in ("title", "explanation"):
            raw = reviewed_report_payload()
            raw["presentation"]["sections"][0][field] += " Changed after review."
            with self.subTest(field=field), self.assertRaisesRegex(ValidationError, "exact presentation"):
                ReviewedReport.model_validate(raw)

    def test_final_gate_rejects_wrong_review_identity_hash_or_stage(self):
        for changes in (
            {"assessment_id": "another-assessment"},
            {"assessment_fingerprint": "c" * 64},
            {"presentation_fingerprint": "d" * 64},
            {"stage": "risk_review", "presentation_fingerprint": None},
        ):
            raw = reviewed_report_payload()
            raw["manager_review"].update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValidationError):
                ReviewedReport.model_validate(raw)

    def test_final_gate_rejects_revise_and_needs_review(self):
        for decision in ("revise", "needs_review"):
            raw = reviewed_report_payload()
            raw["manager_review"]["decision"] = decision
            raw["manager_review"]["findings"][0]["decision"] = decision
            with self.subTest(decision=decision), self.assertRaises(ValidationError):
                ReviewedReport.model_validate(raw)

    def test_final_gate_requires_report_fidelity_pass_for_each_reported_risk(self):
        bundle = bundle_payload(two_risks=True)
        for missing_id in ("risk-1", "risk-2"):
            raw = reviewed_report_payload(bundle)
            raw["manager_review"]["findings"] = [
                finding for finding in raw["manager_review"]["findings"] if finding["risk_id"] != missing_id
            ]
            with self.subTest(missing_id=missing_id), self.assertRaises(ValidationError):
                ReviewedReport.model_validate(raw)
        raw = reviewed_report_payload(bundle)
        raw["manager_review"]["findings"] = [finding_payload("report_fidelity", None)]
        with self.assertRaises(ValidationError):
            ReviewedReport.model_validate(raw)

    def test_final_gate_rejects_unknown_risk_ids_even_when_every_known_risk_passes(self):
        raw = reviewed_report_payload()
        raw["manager_review"]["findings"].append(finding_payload("report_fidelity", "unknown-risk"))
        with self.assertRaisesRegex(ValidationError, "unknown risk ID"):
            ReviewedReport.model_validate(raw)

    def test_empty_final_report_requires_passed_overall_coverage(self):
        bundle = bundle_payload(empty=True)
        report = ReviewedReport.model_validate(reviewed_report_payload(bundle))
        self.assertEqual(report.presentation.sections, ())
        for finding in (finding_payload("report_fidelity", None), finding_payload("coverage", "risk-1")):
            raw = reviewed_report_payload(bundle)
            raw["manager_review"]["findings"] = [finding]
            with self.subTest(finding=finding), self.assertRaises(ValidationError):
                ReviewedReport.model_validate(raw)

    def test_final_gate_revalidates_presentation_coverage_and_prior_handoff(self):
        raw = reviewed_report_payload()
        raw["presentation"]["sections"] = []
        raw["manager_review"]["presentation_fingerprint"] = presentation_fingerprint(raw["presentation"])
        with self.assertRaisesRegex(ValidationError, "every reviewed risk exactly once"):
            ReviewedReport.model_validate(raw)
        raw = reviewed_report_payload()
        raw["handoff"]["manager_review"]["findings"] = [finding_payload("coverage")]
        with self.assertRaises(ValidationError):
            ReviewedReport.model_validate(raw)


class LegacyDetectionCompatibilityTests(unittest.TestCase):
    def test_v1_detection_schema_still_describes_the_unchanged_adapter_payload(self):
        schema = Detection.model_json_schema()
        self.assertEqual(set(schema["properties"]), {"risks", "limitations"})
        self.assertEqual(set(schema["required"]), {"risks", "limitations"})
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["risks"]["maxItems"], 8)
        self.assertEqual(schema["properties"]["limitations"]["maxItems"], 12)
        risk_schema = schema["$defs"]["Risk"]
        fields = {"id", "risk_type", "claim", "rationale", "suggested_action", "target_item_ids",
                  "citations", "severity"}
        self.assertEqual(set(risk_schema["properties"]), fields)
        self.assertEqual(set(risk_schema["required"]), fields)
        self.assertEqual(risk_schema["properties"]["severity"]["enum"], ["low", "medium", "high"])
        self.assertEqual(risk_schema["properties"]["citations"]["minItems"], 2)
        self.assertEqual(schema["$defs"]["Citation"]["properties"]["quote"]["maxLength"], 500)

    def test_legacy_detection_validates_without_v2_fields_or_company_policy(self):
        risk = risk_payload()
        del risk["confidence"]
        del risk["risk_level"]
        risk["severity"] = "medium"
        raw = {"risks": [risk], "limitations": ["Synthetic historical scope."]}
        payload = {
            "plan": {"as_of": "2020-01-01T00:00:00Z", "root": {"id": "PLAN-1"}, "members": []},
            "prior_work": [
                {"id": "PRIOR-1", "created_at": "2019-01-01T00:00:00Z", "unknown_fields": [],
                 "fields": {"title": "Protocol rejects an empty identifier", "description": None}},
                {"id": "PRIOR-2", "created_at": "2019-01-02T00:00:00Z", "unknown_fields": [],
                 "fields": {"title": "Identifier contract", "description": "Identifiers must be populated before submission."}},
            ],
            "allowed_risk_types": ["integration"],
        }
        self.assertEqual(Detection.model_validate(raw).model_dump(), raw)
        self.assertEqual(validate_detection(raw, payload), {**raw, "rejected": []})
        with self.assertRaises(ValidationError):
            Detection.model_validate({**raw, "assessment_id": "v2-is-separate"})
        with self.assertRaises(ValidationError):
            Detection.model_validate({**raw, "risks": [{**risk, "confidence": confidence_payload()}]})


if __name__ == "__main__":
    unittest.main()
