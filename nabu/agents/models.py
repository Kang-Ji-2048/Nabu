import json
import os

from langchain_core.messages import AIMessage, ToolMessage

from .contracts import CriticVerdict
from .evidence import tokens


class OfflineSmokeModel:
    """A scripted plumbing check, explicitly not an AI risk prediction."""

    def bind_tools(self, tools):
        return self

    def with_structured_output(self, schema):
        return self

    def invoke(self, messages):
        names = {message.name for message in messages if isinstance(message, ToolMessage)}
        if "get_plan" not in names:
            return AIMessage(content="", tool_calls=[{"name": "get_plan", "args": {}, "id": "offline-plan"}])
        if "search_prior_work" not in names:
            plan = json.loads(next(message.content for message in messages if isinstance(message, ToolMessage) and message.name == "get_plan"))
            words = tokens(str(plan["root"]["fields"].get("title") or "") + " " + str(plan["root"]["fields"].get("description") or ""))
            return AIMessage(content="", tool_calls=[{"name": "search_prior_work", "args": {"query": " ".join(sorted(words))[:500] or "delivery", "limit": 3}, "id": "offline-search"}])
        return AIMessage(content="", tool_calls=[{"name": "submit_findings", "args": {"findings": [], "limitations": ["Offline smoke test: no AI analysis was performed; zero findings is not a statement that the plan has no risks."]}, "id": "offline-submit"}])


def make_model(mode, model_id):
    if mode == "offline":
        return OfflineSmokeModel()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise ValueError("Set ANTHROPIC_API_KEY for a live review, or use --offline for a plumbing check")
    if not model_id:
        raise ValueError("Set --model or NABU_MODEL to an Anthropic model ID available to your account")
    from langchain_anthropic import ChatAnthropic
    return ChatAnthropic(model=model_id, temperature=0, max_tokens=4096, timeout=90, max_retries=2)
