# Checkpoint

Task: restore efficient caching for vaulted variable file reads in DataLoader.load_from_file.

Status: inspecting repository and tests. Applying test-driven development: add regression test, verify red, implement, verify green, run existing suite.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` and `find` for local search.

Red checks: loader cache tests failed because `cache='none'` and `cache='vaulted'` on plain files populated `_FILE_CACHE`; vars manager integration test failed because changed file content was reloaded.

Green checks: `PYTHONPATH=lib:test/units python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py` passed (43 tests). `git diff --check` passed. Running broader suite next.

Broader-suite attempt: `PYTHONPATH=lib:test/units python -m pytest -q` collected 3820 items with 22 collection errors, then exited 137 while running integration targets (process killed). Exact collection error details were not emitted before termination. This run did not pass; integration-wide status remains uncertain. Running unit tests separately.

Unit-suite attempt: `PYTHONPATH=lib:test/units python -m pytest -q test/units` reached unrelated CLI/Galaxy failures and errors by 3% progress; interrupted after 16.16s to avoid extensive automatic reruns. At interruption: 9 failed, 94 passed, 34 errors, 131 rerun, 138 warnings. Failures were `test_execute_list_collection_no_valid_paths` in `test/units/cli/galaxy/test_execute_list_collection.py`; `test_simple_command`, `test_no_argument`, `test_did_you_mean_playbook`, `test_run_import_playbook` in `test/units/cli/test_adhoc.py`; `TestConsoleCLI.test_helpdefault`, `TestConsoleCLI.test_module_args` in `test/units/cli/test_console.py`; and `test_builtin_modules_list`, `test_legacy_modules_list` in `test/units/cli/test_doc.py`. The 34 setup errors were in `test/units/cli/test_galaxy.py`, where `Galaxy()` gets a `None` CLI type and `os.path.join` raises `TypeError`. These were outside the changed loader/vars paths. The full unit suite did not pass; later tests were not run.

Related-suite check: `PYTHONPATH=lib:test/units python -m pytest -q test/units/parsing test/units/vars` passed (340 tests, one `AnsibleCollectionFinder has already been configured` warning from `test_mod_args.py`). `git diff --check` passed. All changes remain in checked-out files; no git history or index changes.
