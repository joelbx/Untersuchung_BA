Task: Update scripts/affiliate_server.py queue items to support ISBN and ASIN with identifier-based equality, staging, and complete serialization.
Status: Implemented PrioritizedIdentifier with identifier-only equality/hash, JSON serialization, stage_import, queue deduplication, and selective import staging. Kept PrioritizedISBN as a compatibility wrapper.
Verification: scripts/tests/test_affiliate_server.py (18 passed); ruff check passed; git diff --check passed. Ruff format --check reports existing file-wide style differences, so no broad reformat was applied.
