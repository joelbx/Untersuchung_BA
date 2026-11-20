# Checkpoint

Implemented undefined-value YAML representation and filter error wrapping. The `AnsibleUndefined` representer calls `bool(data)`, causing Jinja `UndefinedError` with the variable name. Both YAML filters raise `AnsibleFilterError` with the filter name, `orig_exc`, and exception chaining.

TDD red: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py` failed in three new cases: direct dump raised `RepresenterError`; both filters leaked `RepresenterError`.

TDD green: the same command passed (14 tests). `PYTEST_ADDOPTS='' PYTHONPATH=lib:test python -m pytest -q -p no:rerunfailures test/units/parsing/yaml/test_dumper.py test/units/plugins/filter test/units/template` passed (127 tests, six existing deprecation warnings). A direct Templar check for `{{ MYSVC_ENV | to_nice_yaml }}` produced `AnsibleFilterError` with `MYSVC_ENV` in its message and Jinja `UndefinedError` in both `orig_exc` and `__cause__`.

Full suite command: `PYTHONPATH=lib:test python -m pytest -q`. It collected 3623 items with 20 collection errors, then showed many unrelated failures/errors (including `test/units/cli/test_adhoc.py::test_simple_command` KeyError and `test/units/cli/test_cli.py::TestCliBuildVaultIds::test` AttributeError). Interrupted after 19.55 seconds because the full run was repeating failures; at interruption it reported 37 failed, 63 passed, 44 errors, and 184 reruns. Collection errors included `test/ansible_test/unit/test_diff.py` (`No module named 'ansible_test._internal'`) and `test/ansible_test/validate-modules-unit/test_validate_modules_regex.py` (`No module named 'validate_modules'`). Overall full-suite status remains unknown because the run was interrupted.

Related broader command: `PYTEST_ADDOPTS='' PYTHONPATH=lib:test python -m pytest -q -p no:rerunfailures test/units/parsing/yaml test/units/plugins/filter test/units/template` reported 161 passed and one error: `test/units/parsing/yaml/test_constructor.py::test_duplicate_yaml_dict_key_error` could not find fixture `mocker`; 14 pre-existing deprecation warnings. The scoped follow-up above excludes that unrelated constructor test.

Attempted `PYTHONPATH=lib:test python -m pytest -q -p no:rerunfailures test/units/parsing/yaml test/units/plugins/filter test/units/template` and the same command with `-o addopts=''`; both failed before collection with `unrecognized arguments: --reruns=3` because the environment's `PYTEST_ADDOPTS` requires the rerun plugin. Explicit `PYTEST_ADDOPTS=''` resolved that tooling issue.
