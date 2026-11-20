# Checkpoint

Task: surface undefined-variable errors during YAML dumping and wrap YAML filter failures.

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find. No external research or downloads.

Implementation: `AnsibleDumper` registers `represent_undefined`, which evaluates `bool(data)` so Jinja raises `UndefinedError`. The YAML filters preserve that exception for `Templar` to convert to `AnsibleUndefinedVariable`; other dump failures become `AnsibleFilterError` with `orig_exc`.

Verification:

- `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml/test_dumper.py test/units/parsing/yaml/test_loader.py test/units/parsing/yaml/test_objects.py test/units/plugins/filter/test_core.py test/units/template/test_templar.py`: 96 passed, exit 0.
- `git diff --check`: exit 0.
- Broader command `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml test/units/plugins/filter/test_core.py test/units/template/test_templar.py`: exit 1, with 98 passed and one setup error in `test/units/parsing/yaml/test_constructor.py::test_duplicate_yaml_dict_key_error`: `fixture 'mocker' not found`. That constructor test remains unverified in this environment; no dependencies were downloaded.
