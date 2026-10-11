"""Check whether a response's claims match a set of reference facts."""
import re
from dataclasses import dataclass


@dataclass
class Verdict:
    key: str
    expected: str
    status: str  # "supported", "contradicted", or "unverifiable"


def _sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def check_claims(response, facts):
    """
    facts maps a key phrase to its correct answer,
    e.g. {"capital of Nigeria": "Abuja"}.

    A fact is 'supported' if a sentence mentions the key phrase and also
    contains the correct answer. It is 'contradicted' if the key phrase is
    mentioned but the correct answer is not. It is 'unverifiable' if the
    response never mentions the key phrase.
    """
    sentences = _sentences(response)
    verdicts = []
    for key, expected in facts.items():
        relevant = [s for s in sentences if key.lower() in s.lower()]
        if not relevant:
            status = "unverifiable"
        elif any(expected.lower() in s.lower() for s in relevant):
            status = "supported"
        else:
            status = "contradicted"
        verdicts.append(Verdict(key, expected, status))
    return verdicts
