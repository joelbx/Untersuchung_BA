# Checkpoint

Resolved Windows SSH stderr CLIXML replacement. `_replace_stderr_clixml` preserves surrounding bytes and malformed or incomplete blocks, handles nested headers and adjacent XML objects, and decodes UTF-8 with cp437 fallback. `_STRING_DESERIAL_FIND` now matches explicit UTF-16-BE byte pairs so Unicode lookalikes remain literal.

Verification:
- `PYTHONPATH=lib pytest -q -o addopts='' test/units/plugins/connection test/units/plugins/shell`: 106 passed.
- `git diff --check`: passed.
- `PYTHONPATH=lib pytest -q -o addopts=''`: collection fails (exit 3). `test/integration/targets/async/library/async_test.py` executes as a module without JSON stdin; `AnsibleModule._load_params()` raises `SystemExit: 1` after JSONDecodeError. It does not run the full suite, so repository-wide status remains unknown.
- `PYTHONPATH=lib pytest -q -o addopts='' test/units`: stopped after 13.46 seconds due to repeated unrelated CLI failures; observed 9 failed, 96 passed, 39 errors, 146 reruns before interruption. Failures shown in `test/units/cli/galaxy/test_execute_list_collection.py`, `test/units/cli/test_adhoc.py`, `test/units/cli/test_console.py`, and `test/units/cli/test_doc.py`; errors in `test/units/cli/test_galaxy.py` included `TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'` at `ansible/galaxy/__init__.py:59` because `context.CLIARGS.get('type')` was None. Full unit suite status remains unknown.
