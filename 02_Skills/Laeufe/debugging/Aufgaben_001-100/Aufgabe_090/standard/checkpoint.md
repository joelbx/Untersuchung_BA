# Checkpoint

Investigating `/lists/add` POST/query precedence and flattened input reconstruction. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and file inspection. No fix attempted yet.

Root cause: `ListRecord.from_input` obtains values through `web.input`, whose `rawinput` merges query and body (`dictadd(b, a)`); defaults include `seeds=[]`. `utils.unflatten` preserves the first simple-key assignment and uses `setdefault` for nested fields, so a default/simple `seeds` collides with `seeds--*`. The seed normalizer also indexes `seed['key']` before validating partial nested items. A body-only `parse_qs` path with ancestor-aware defaults and last-write semantics is needed.

Regression tests were written and run before implementation; the POST isolation and nested seed tests failed at `web.input`, and the unflatten test failed because the first value won. The first patch exposed that `parse_qs(bytes)` returns bytes keys; decoding the body before parsing resolved it. Focused list and upstream utility tests passed (19 tests). `python -m black --check openlibrary/plugins/openlibrary/lists.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/utils.py` could not run: `/usr/local/bin/python: No module named black`. Formatting remains unverified by Black; Ruff and diff checks are available.

Final verification: `python -m pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` passed (19); `python -m ruff check openlibrary/plugins/openlibrary/lists.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/utils.py` passed; `git diff --check` passed. The pytest run reports one existing `cgi` deprecation warning from web.py.
