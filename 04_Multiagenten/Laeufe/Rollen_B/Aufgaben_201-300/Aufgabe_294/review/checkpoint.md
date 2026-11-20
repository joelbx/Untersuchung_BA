VERDICT: FIX

Review complete. CODE_DEFECT: `_extract_tar_file` (lines 1401-1404) and `_extract_tar_dir` (lines 1434-1437) call `os.makedirs` before `_is_child_path`. If `dest/escape` is a symlink outside and the member is `escape/new/file`, creating the missing parent creates `outside/new` before rejection. Validate the resolved parent before any directory creation, then validate again before the final write. The current test covers only a direct symlink parent that already exists.

Tests executed: `PYTHONPATH=lib:test python3 -m pytest -q test/units/galaxy/test_collection.py` — 62 passed; `PYTHONPATH=lib:test python3 -m pytest -q test/units/galaxy` — 150 passed. TEST_ENVIRONMENT_PROBLEM: none. No project code or tests changed during review.
