"""Shared model-visible ticket text and explicit truncation limits."""
import re

STOPWORDS = set("a an the and or to of in on for with by is are be as it this that should can from into at".split())


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.casefold())) - STOPWORDS


def text_of(item):
    return "\n".join(str(item["fields"][name]) for name in ("title", "description")
                     if name not in item["unknown_fields"] and item["fields"][name] is not None)


def bounded_item(item):
    item = {**item, "fields": dict(item["fields"])}
    truncated = []
    for name, limit in (("title", 500), ("description", 4000)):
        value = item["fields"][name]
        if isinstance(value, str) and len(value) > limit:
            item["fields"][name] = value[:limit]
            truncated.append(name)
    item["truncated_fields"] = truncated
    return item
