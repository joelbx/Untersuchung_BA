# Checkpoint

Task: repair `incdec_number` URL segment selection, encoded triplet handling, decrement bounds, count validation, and encoded data preservation.

Implementation: path-only default; path/query/anchor/host priority; first eligible numeric run in the first selected segment; port ignored; encoded triplet digits excluded; `QUrl.FullyEncoded` getters and `QUrl.StrictMode` setters; positive integer count; leading zero width retained.

Verification:
- `git diff --check`: passed.
- `QT_QPA_PLATFORM=offscreen pytest -o addopts='' -o filterwarnings='' -q tests/unit/utils/test_urlutils.py --disable-warnings --maxfail=1`: 348 passed, 1 skipped (exit 0).
- `pytest -o addopts='' -o filterwarnings='' -q tests/unit/utils/test_urlutils.py -k incdec --disable-warnings --maxfail=1`: 128 passed (before two final tests were added).

Environment limitations encountered:
- `pytest -q tests/unit/utils/test_urlutils.py -k incdec --disable-warnings --maxfail=1` failed during pytest startup with `PytestRemovedIn8Warning: The --strict option is deprecated, use --strict-markers instead.` The repository's pytest.ini supplies `--strict`; command-line overrides avoid it.
- `pytest -o addopts='' -o filterwarnings='' -q tests/unit/utils/test_urlutils.py --disable-warnings --maxfail=1` aborted (exit 134) when the pytest-qt qapp fixture started without a display. `QT_QPA_PLATFORM=offscreen` resolves the test environment issue.

Requirement interpretation: the final explicit requirement to modify the first numeric match in path, query, anchor, host priority governs the earlier contradictory wording about the last numeric sequence.
