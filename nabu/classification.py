"""Deterministic ingestion work topics, separate from learned risk detection."""
from .text import tokens

VERSION = "work-topics-v1"
TOPICS = {
    "security": {"security", "authentication", "authorization", "credentials", "permission", "encryption"},
    "deployment": {"deploy", "deployment", "packaging", "package", "container", "runtime", "release"},
    "testing": {"test", "tests", "testing", "verification", "regression"},
    "data": {"database", "sql", "schema", "migration", "storage", "stream", "batch"},
    "integration": {"api", "connector", "integration", "endpoint", "protocol"},
    "performance": {"performance", "latency", "throughput", "memory", "optimization"},
    "interface": {"ui", "dashboard", "screen", "layout", "button"},
    "documentation": {"documentation", "docs", "guide", "readme"},
}


def classify(title, description=None):
    words = tokens(str(title or "") + " " + str(description or ""))
    scores = [(len(words & cues), topic) for topic, cues in TOPICS.items()]
    score, topic = max(scores, key=lambda pair: (pair[0], pair[1]))
    return topic if score else "unassigned"
