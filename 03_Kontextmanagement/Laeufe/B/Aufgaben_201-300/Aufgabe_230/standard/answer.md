Updated [affiliate_server.py](/app/scripts/affiliate_server.py) with `PrioritizedIdentifier` for ISBN and ASIN values, identifier based deduplication, `stage_import` handling, and complete JSON serialization. Existing `PrioritizedISBN` callers remain supported.

Verification: **18 affiliate tests passed**; Ruff passed.