# Checkpoint

Task: fix password lookup key=value parameter parsing and chars handling using test-driven development.

Changes: moved parameter parsing into `LookupModule`, source omitted options via `get_option`, initialize options in `run`, allow raw `chars` values so lists reach the parser, and preserve supplied lists. Existing parser tests now use the plugin loader so option definitions are registered.

Red checks observed:
- `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup/test_password.py::TestLookupModuleWithoutPasslib::test_list_chars_option_generates_only_requested_character` failed with `AttributeError: 'list' object has no attribute 'replace'`.
- `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup/test_password.py::TestParseParameters::test` failed with missing instance method.
- `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup/test_password.py::TestParseParameters::test_empty_chars_list_is_preserved` failed because empty list became default chars.

Green check: `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup/test_password.py` — 31 passed.

Repository-wide pytest: running `timeout 120s env PYTHONPATH=lib:test/units python -m pytest -q`; output in `/tmp/password-full-pytest.log`.

Additional verification:
- `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup` — 38 passed.
- `PYTHONPATH=lib python - <<'PY' ... PY` direct lookup check (inline seed repeated; same seed via direct option; length 24) — passed.
- `timeout 120s env PYTHONPATH=lib:test/units python -m pytest -q` — exit 124 after two minutes at about 18% of the suite. The output showed failures/errors in unrelated suites including `test/units/ansible_test/ci/test_azp.py`, `test/units/cli/test_adhoc.py`, `test/units/cli/test_cli.py`, `test/units/cli/test_galaxy.py`, `test/units/config/manager/test_find_ini_config_file.py`, and `test/units/module_utils/basic/test_argument_spec.py`. The timeout prevented a final summary; remaining suite status is unknown. Output: `/tmp/password-full-pytest.log`.
- `PYTHONPATH=lib:test/units python -m pytest -q -x --reruns 0` — exit 1 at collection: `test/ansible_test/unit/test_diff.py` could not import `ansible_test._internal` (`ModuleNotFoundError`). Output: `/tmp/password-first-pytest.log`.
- `git diff --check` — passed.
