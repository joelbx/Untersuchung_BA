# Debugging checkpoint

Task: undefined values passed to YAML filters raise a YAML RepresenterError. Investigating the dumper and filter exception path before editing implementation.

Initial state: working tree clean (`git status --short` produced no entries).

Root cause: `AnsibleDumper` has representers for custom data types but none for `AnsibleUndefined`. PyYAML therefore raises `RepresenterError` before Jinja's `StrictUndefined.__bool__` can raise `UndefinedError`. Both YAML filters pass that exception through. `Templar.do_template` converts direct `UndefinedError` to `AnsibleUndefinedVariable`, but cannot recognize one wrapped by `AnsibleFilterError` without tracing `orig_exc`.

Hypothesis: register an exact `AnsibleUndefined` representer that evaluates `bool(data)`; wrap filter failures with `AnsibleFilterError` and `orig_exc`; have templating recognize this specific wrapped `UndefinedError` so its public error remains `AnsibleUndefinedVariable`. Preserve the filter exception as the cause.

Regression tests were written and run before implementation: four cases failed with `yaml.representer.RepresenterError` as expected. After implementation, the focused modules passed (61 tests).

Broader check: `PYTHONPATH=lib:test python -m pytest -q -o addopts='' test/units/parsing/yaml test/units/plugins/filter test/units/template/test_templar.py` exited 1: 144 passed, 1 setup error in `test_duplicate_yaml_dict_key_error`, because fixture `mocker` is unavailable. This is an offline tooling limitation; that one test remains unverified. No dependency downloads attempted.

Final check: `PYTHONPATH=lib:test python -m pytest -q -o addopts='' test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py test/units/template/test_templar.py && git diff --check` exited 0; 61 tests passed.
