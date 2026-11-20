# Checkpoint

Task: Fix `make_work()` for documents missing author fields; update `make_author()` type annotations and return behavior.

Completed:
- Annotated `make_work(doc: dict) -> web.Storage` and nested `make_author(key: str, name: str) -> Author`.
- Paired available author keys and names, producing an empty list when either is missing or `None`.
- Preserved supplied `cover_url`; defaulted absent `cover_url`, `ia`, and `first_publish_year`.
- Added regression tests for missing author fields, `None` author field, multiple authors, and supplied metadata.

Verification: `python -m pytest openlibrary/plugins/upstream/tests -q` passed (49 passed, 5 xfailed). `git diff --check` passed.
