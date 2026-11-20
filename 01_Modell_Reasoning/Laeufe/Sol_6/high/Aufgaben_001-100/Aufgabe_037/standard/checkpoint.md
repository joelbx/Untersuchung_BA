# Checkpoint

Task: make YAML dumping of `AnsibleUndefined` surface an undefined-variable error and wrap `to_yaml` / `to_nice_yaml` failures as `AnsibleFilterError`.

Status: complete. Added an `AnsibleUndefined` representer that calls `bool(data)`, added filter-specific error wrapping with `orig_exc`, and added unit coverage for direct/nested undefined values, other dump failures, and template rendering.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py test/units/template/test_templar.py` passed (64 tests). `git diff --check` passed.
