# Import preview checkpoint

Status: investigating the existing import pipeline and tests before edits.
Root cause: both import branches allocate persistent keys and invoke write/cover/IA operations directly; no shared save flag exists. `process_cover_url` embeds host checking, and the requested public converter names are absent.
Pattern: `load_data` already collects new author/work/edition dictionaries in `edits`; matched imports collect modified records similarly. Preview can return those same records while guarding side effects.
Hypothesis: passing `save=False` through key allocation, cover, and write boundaries will preserve construction while eliminating writes. The added regression test fails at collection as expected because `check_cover_url_host` is absent (`pytest -q openlibrary/catalog/add_book/tests/test_preview.py`, exit 1).
Implementation: added UUID preview keys, shared author edit collection, explicit cover host validation and preview acceptance reporting, write/IA/cover guards, endpoint flag propagation, and converter interfaces. The matched-work path now creates and reports author candidates. Author lookup continues to alternate-name queries after a date mismatch.
Checks: initial full relevant run failed 1 existing cover test because its fixture used a now-disallowed host; changed the fixture to an allowed Amazon host. A later run failed 1 matching test because the converter stopped normalizing the source record in place; restored the existing matching behavior. Another added test exposed an alternate-name fallback gap; fixed the query loop. An added malformed-cover test failed with `ValueError: Invalid IPv6 URL`; the host validator now returns False.
Final checks: `pytest -q openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests/test_code.py` (171 passed, exit 0); `ruff check` on edited Python files (exit 0); `git diff --check` (exit 0). Warnings are existing deprecations from pytest-asyncio, Genshi, dateutil, and Pydantic.
Constraint: local repository only; no downloads or external research.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.
