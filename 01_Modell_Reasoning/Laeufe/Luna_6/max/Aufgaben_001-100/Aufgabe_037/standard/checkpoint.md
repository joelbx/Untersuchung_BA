# Checkpoint

Task: Fix YAML dumping of `AnsibleUndefined` so `to_yaml` and `to_nice_yaml` surface a clear filter error while preserving the undefined-variable cause.

Changes:
- Registered `represent_undefined` with `AnsibleDumper`; its `bool(data)` call triggers Jinja's `StrictUndefined` error.
- Both YAML filters re-raise Jinja `UndefinedError` for the templating layer to translate and wrap other dump failures in filter-specific `AnsibleFilterError` objects with `orig_exc` preserved.

Verification:
- `python -m pytest test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py` — 11 passed.
- Manual checks verified undefined values are not serialized, Templar raises `AnsibleUndefinedVariable` with the original `UndefinedError` in its exception context, unsupported objects produce filter-specific `AnsibleFilterError` with the original `RepresenterError`, and dicts still round-trip through both YAML filters.
- `git diff --check` — clean.
