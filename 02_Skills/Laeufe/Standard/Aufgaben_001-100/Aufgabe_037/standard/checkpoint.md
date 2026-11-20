# Checkpoint

Implemented `AnsibleUndefined` YAML representer that evaluates the value and raises Jinja's undefined error. Both YAML filters now raise `AnsibleFilterError` with the original exception in `orig_exc`. Templar converts filter errors caused by undefined values to `AnsibleUndefinedVariable`, preserving the underlying `UndefinedError` in `orig_exc` and honoring `fail_on_undefined=False`.

Verification:
- `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py`: 18 passed.
- `PYTHONPATH=lib:test python -m pytest -q test/units/template/test_templar.py test/units/parsing/yaml/test_dumper.py test/units/parsing/yaml/test_loader.py test/units/parsing/yaml/test_objects.py test/units/plugins/filter`: 145 passed.
- `git diff --check`: passed.

Offline tooling limitation:
- Command: `PYTHONPATH=lib:test python -m pytest -q test/units/template/test_templar.py test/units/parsing/yaml test/units/plugins/filter`
- Result: 147 passed, 1 error, 3 rerun. `test/units/parsing/yaml/test_constructor.py::test_duplicate_yaml_dict_key_error` could not run because fixture `mocker` is unavailable (`fixture 'mocker' not found`). The constructor test remains unverified in this environment; no dependency was downloaded.
