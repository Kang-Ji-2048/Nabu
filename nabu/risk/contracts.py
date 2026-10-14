from typing import Literal

from pydantic import Field, model_validator

from ..agents.contracts import Citation, StrictModel


class ModelManifest(StrictModel):
    version: Literal["nabu-slm-v1"]
    model: str = Field(min_length=1, max_length=200)
    trained: bool
    trained_through: str
    training_data_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    artifact_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    risk_types: list[str] = Field(min_length=1, max_length=20)

    @model_validator(mode="after")
    def unique_types(self):
        if len(set(self.risk_types)) != len(self.risk_types) or any(not t.strip() for t in self.risk_types):
            raise ValueError("Risk types must be nonempty and unique")
        return self


class Risk(StrictModel):
    id: str = Field(min_length=1, max_length=80)
    risk_type: str = Field(min_length=1, max_length=100)
    claim: str = Field(min_length=1, max_length=1500)
    rationale: str = Field(min_length=1, max_length=3000)
    suggested_action: str = Field(min_length=1, max_length=1500)
    target_item_ids: list[str] = Field(min_length=1, max_length=10)
    citations: list[Citation] = Field(min_length=2, max_length=10)
    severity: Literal["low", "medium", "high"]


class Detection(StrictModel):
    risks: list[Risk] = Field(max_length=8)
    limitations: list[str] = Field(max_length=12)

    @model_validator(mode="after")
    def unique_ids(self):
        if len({r.id for r in self.risks}) != len(self.risks):
            raise ValueError("Risk IDs must be unique")
        return self


class ReportSection(StrictModel):
    risk_id: str
    title: str = Field(min_length=1, max_length=200)
    explanation: str = Field(min_length=1, max_length=2000)
    recommended_action: str = Field(min_length=1, max_length=1500)


class Presentation(StrictModel):
    sections: list[ReportSection] = Field(max_length=8)
