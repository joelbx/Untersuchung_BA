# Checkpoint

Task: fix undefined-variable handling in YAML dumping and the `to_yaml` / `to_nice_yaml` filters.

Initial state: working tree clean. `rg` is unavailable, so repository searches will use `find` and `grep`.

Next: inspect local instructions, implementation, and existing tests; edit checked-out files; run relevant existing tests.

Implementation: registered `AnsibleUndefined` in `AnsibleDumper` using `bool(data)`; YAML filters now wrap failures with `AnsibleFilterError` and `orig_exc`; templating converts filter errors caused by undefined variables into `AnsibleUndefinedVariable` and retains the Jinja exception. Added focused regression tests.

Verification: the focused 64 tests passed. The broader YAML/filter/template suite passed 165 tests and had one setup error because this environment lacks the existing `mocker` fixture used by `test_duplicate_yaml_dict_key_error`. The diff passes `git diff --check`.

Final verification: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml test/units/plugins/filter test/units/template -k 'not test_duplicate_yaml_dict_key_error'` passed: 165 tests, 1 deselected. The deselected test cannot run here because its existing `mocker` fixture is unavailable. No downloads or fixture changes were made.
