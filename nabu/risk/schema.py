"""Export versioned contracts without changing the trained v1 detector schema."""

CONTRACT_NAMES = (
    "detection", "workflow", "assessment", "company-policy",
    "manager-review", "report-handoff", "presentation", "reviewed-report",
)


def risk_schema(contract="detection"):
    if contract not in CONTRACT_NAMES:
        raise ValueError(f"Unknown risk contract: {contract}")
    if contract == "detection":
        from .contracts import Detection
        return Detection.model_json_schema(), "nabu-assess-v1"

    from pydantic.json_schema import models_json_schema
    from .contracts_v2 import (
        AssessmentBundle, CompanyRiskPolicy, ManagerReview, PresentationV2,
        ReportHandoff, ReviewedReport,
    )

    contracts = {
        "assessment": (AssessmentBundle, "nabu-assessment-v2"),
        "company-policy": (CompanyRiskPolicy, "nabu-risk-policy-v1"),
        "manager-review": (ManagerReview, "nabu-manager-review-v1"),
        "report-handoff": (ReportHandoff, "nabu-report-handoff-v2"),
        "presentation": (PresentationV2, "nabu-presentation-v2"),
        "reviewed-report": (ReviewedReport, "nabu-reviewed-report-v2"),
    }
    if contract != "workflow":
        model, version = contracts[contract]
        return model.model_json_schema(), version

    models = [(model, "validation") for model, _ in contracts.values()]
    references, definitions = models_json_schema(models, title="Nabu risk workflow v2")
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:nabu:risk-workflow:v2",
        **definitions,
        "oneOf": [references[key] for key in models],
    }
    return schema, "nabu-risk-workflow-v2"
