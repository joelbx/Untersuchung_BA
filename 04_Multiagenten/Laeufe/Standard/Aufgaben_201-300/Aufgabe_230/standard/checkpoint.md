Task: Expand PrioritizedISBN into PrioritizedIdentifier for ISBN/ASIN support, identifier-based equality/hash, stage_import, complete serialization, and compatibility.
Status: Implemented and verified. PrioritizedIdentifier now has generic identifier, stage_import, identifier-based equality/hash, and JSON-safe to_dict. Legacy PrioritizedISBN constructor and isbn property remain available. Submission deduplicates queue items and accepts stage_import=false; lookup carries staging choices to batch processing.
Validation: pytest -q scripts/tests/test_affiliate_server.py (18 passed); ruff check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py (passed); git diff --check (passed).
Constraints observed: Local repository only; no git history/index/harness changes.
