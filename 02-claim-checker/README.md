# Claim Checker

Takes a model's response and a short list of reference facts. It reports whether each fact is supported, contradicted, or not addressed at all.

This is a simple version of fact-checking. It does not search the web. It checks against facts you provide, which is how many evaluation teams start before adding a retrieval step.

**Skills shown:** fact-checking, analytical reasoning, writing clear verdict logic.

## Run the tests

```
python3 -m unittest -v
```

## Example

```python
from claim_checker import check_claims

facts = {"capital of Nigeria": "Abuja"}
for v in check_claims(response_text, facts):
    print(v.key, "->", v.status)
```

## Known limits

Matching is by substring. If a sentence mentions the topic and the right answer in an unrelated way, it can be marked supported. Use it as a first pass, then review the flagged items by hand.
