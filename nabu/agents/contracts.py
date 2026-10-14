from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Citation(StrictModel):
    item_id: str
    field: Literal["title", "description"]
    quote: str = Field(min_length=1, max_length=500)


class Finding(StrictModel):
    id: str = Field(min_length=1, max_length=80)
    claim: str = Field(min_length=1, max_length=1500)
    rationale: str = Field(min_length=1, max_length=3000)
    suggested_action: str = Field(min_length=1, max_length=1500)
    target_item_ids: list[str] = Field(min_length=1, max_length=10)
    citations: list[Citation] = Field(min_length=2, max_length=10)
    severity: Literal["low", "medium", "high"]
    scope_basis: Literal["not_visible_in_observed_scope"]


class Submission(StrictModel):
    findings: list[Finding] = Field(max_length=8)
    limitations: list[str] = Field(max_length=12)

    @model_validator(mode="after")
    def unique_findings(self):
        if len({finding.id for finding in self.findings}) != len(self.findings):
            raise ValueError("Finding IDs must be unique")
        return self


class Decision(StrictModel):
    finding_id: str
    action: Literal["accept", "revise", "drop"]
    reason: str = Field(min_length=1, max_length=2000)


class CriticVerdict(StrictModel):
    decisions: list[Decision] = Field(max_length=8)


class EmptyArgs(StrictModel):
    pass


class SearchArgs(StrictModel):
    query: str = Field(min_length=1, max_length=500)
    limit: int = Field(default=5, ge=1, le=10)
    completed_only: bool = True


class ItemArgs(StrictModel):
    item_id: str


class PatternArgs(StrictModel):
    item_ids: list[str] = Field(min_length=1, max_length=20)
    term: str = Field(min_length=1, max_length=100)


TOOLS = {
    "get_plan": (EmptyArgs, "Read the frozen historical plan and its unknown fields."),
    "search_prior_work": (SearchArgs, "Search cutoff-bound earlier ticket text for supporting examples OR counterexamples. Uses the run's fixed lexical or semantic retrieval. Similarity/categories are not proof of comparability. completed_only means historically observed done status, not successful delivery."),
    "get_item": (ItemArgs, "Inspect a prior ticket at this review's fixed cutoff. No later fields are available."),
    "inspect_scope": (ItemArgs, "Inspect observed membership of an earlier epic at the fixed cutoff; incomplete scope stays explicit."),
    "measure_pattern": (PatternArgs, "Count literal phrase matches in previously inspected ticket text. Reports missing text; counts are descriptive, not probabilities or causal proof."),
    "submit_findings": (Submission, "Submit the complete finding set, including previously accepted findings, with exact evidence quotes and limitations. Call this tool alone, never with another tool in the same message."),
}


def tool_specs():
    return [{"name": name, "description": description, "parameters": schema.model_json_schema()}
            for name, (schema, description) in TOOLS.items()]
