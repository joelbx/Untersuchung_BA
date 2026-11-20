# Checkpoint

Task: add Amazon edition language metadata to `serialize(product)` and preserve the `languages` field in cleaned Amazon metadata.

Completed: the serializer reads `content_info.languages.display_values`, excludes entries whose type is `Original Language`, retains each displayed name exactly once in source order, and omits `languages` when no values remain. The metadata cleaner now accepts `languages`.

Verification: `python -m pytest openlibrary/tests/core/test_vendors.py -q` passed (33 tests; existing deprecation warnings only).
