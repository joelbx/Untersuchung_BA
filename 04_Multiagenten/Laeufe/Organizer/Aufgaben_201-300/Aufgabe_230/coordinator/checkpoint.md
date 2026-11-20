# Checkpoint

Completed: Introduced PrioritizedIdentifier with generic identifier, stage_import, identifier-only equality/hash, queue ordering, and complete JSON-safe to_dict(). Preserved PrioritizedISBN as an alias plus its old keyword and positional constructor forms. Queue processing now deduplicates identifiers and honors stage_import when staging import items.

Verification: `pytest -q scripts/tests/test_affiliate_server.py` (18 passed); `python -m ruff check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py` (passed); `git diff --check` (passed).

Delegation: None; solved directly.
