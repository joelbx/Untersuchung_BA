VERDICT: FIX

**Code defect:** [_extract_tar_file](/app/lib/ansible/galaxy/collection.py:1401) and [_extract_tar_dir](/app/lib/ansible/galaxy/collection.py:1434) create missing parent directories before checking whether the resolved path stays inside the collection. If `dest/escape` links outside and a tar entry needs `escape/new/file`, extraction can create `new` outside the destination before raising an error. Validate the resolved parent before `os.makedirs`, then check again before writing.

Tests executed:

- `PYTHONPATH=lib:test python3 -m pytest -q test/units/galaxy/test_collection.py` — 62 passed.
- `PYTHONPATH=lib:test python3 -m pytest -q test/units/galaxy` — 150 passed.

TEST_ENVIRONMENT_PROBLEM: none. I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code or tests were changed during this independent review.