# Checkpoint

Task: resolve undefined-value handling in YAML filters and the Ansible YAML dumper.

Progress: repository inspection started. Next: locate repository guidance, implementations, and existing tests; implement and run relevant tests.

Findings: `AnsibleDumper` lacks an `AnsibleUndefined` representer; `to_yaml` and `to_nice_yaml` call `yaml.dump` without error translation. The templating class derives from Jinja `StrictUndefined`, so the requested `bool(data)` representer triggers its undefined error.

Implementation complete:
- Registered `represent_undefined` for `AnsibleUndefined`; its `bool(data)` call raises Jinja's undefined-variable error during YAML dumping.
- Wrapped YAML dump failures in filter-specific `AnsibleFilterError` messages and retained the original exception as `__cause__`.
- Existing relevant unit tests passed: 11 passed in `test_dumper.py` and `test_core.py`.
- Direct check confirmed each YAML filter raises `AnsibleFilterError` with the undefined variable message and a chained `jinja2.exceptions.UndefinedError` cause.
- `git diff --check` passed.
