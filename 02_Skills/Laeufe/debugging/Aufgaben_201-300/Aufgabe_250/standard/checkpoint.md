# Checkpoint

- Task: add `luqum_replace_child` in `openlibrary/solr/query_utils.py`.
- Status: investigating existing tree helpers and tests before editing implementation.
- Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); use local `grep`/`find`.
- Root cause: `query_utils.py` has removal and traversal helpers but no replacement helper. Luqum's `BaseOperation.children` setter accepts an iterable and stores a tuple; `Group` and `Unary` use the generic setter for one child. Equality is structural (`Item.__eq__`).
- Pattern: `luqum_remove_child` supports `(BaseOperation, Group, Unary)` and raises `ValueError("Not supported for generic class Item")` otherwise.
- Hypothesis: tuple rebuilding with equality substitution, followed by the existing `children` setter, replaces all equal direct children while preserving order. Skipping assignment when absent preserves existing children exactly.
- Reproduction: `python -m pytest openlibrary/tests/solr/test_query_utils.py -q` exits 1 during collection with `ImportError: cannot import name 'luqum_replace_child'`, as expected before implementation.
- Implementation: added `luqum_replace_child` with supported parent guard, equality-based tuple rebuilding, and no assignment when absent.
- Verification: `python -m pytest openlibrary/tests/solr/test_query_utils.py -q` exits 0 (11 passed); `python -m pytest openlibrary/tests/solr -q` exits 0 (79 passed); `git diff --check` exits 0.
