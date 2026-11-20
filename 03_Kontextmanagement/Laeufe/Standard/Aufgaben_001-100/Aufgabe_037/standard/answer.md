Fixed undefined-variable handling for YAML filters. `AnsibleDumper` now triggers Jinja’s undefined error for `AnsibleUndefined`; `to_yaml` and `to_nice_yaml` report filter-specific `AnsibleFilterError`s; and templating surfaces those cases as `AnsibleUndefinedVariable` while preserving the original cause.

Added regression tests. All 65 relevant tests pass, and `git diff --check` is clean.