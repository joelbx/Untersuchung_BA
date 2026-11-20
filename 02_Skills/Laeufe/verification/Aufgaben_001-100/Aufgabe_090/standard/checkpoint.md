# Checkpoint

Task: resolve `/lists/add` POST body/query conflict.

Changes:
- Parse nonempty request body with `urllib.parse.parse_qs`, taking the first value per key, and avoid `web.input()` on that path.
- Apply defaults only to absent form keys with no nested/indexed descendants.
- Ignore empty or malformed reconstructed seed entries.
- Make later simple-key assignments override earlier ones in `unflatten`.
- Add tests for body isolation, first-value handling, indexed seeds, query fallback, and assignment precedence.

Verification (after edits):
- `python -m pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` — exit 0, 18 passed, 1 deprecation warning.
- `python -m ruff check openlibrary/plugins/openlibrary/lists.py openlibrary/plugins/upstream/utils.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` — exit 0.
- `git diff --check` — exit 0.

Tool note: `rg` is unavailable (`/bin/bash: rg: command not found`); local grep/find used instead.
