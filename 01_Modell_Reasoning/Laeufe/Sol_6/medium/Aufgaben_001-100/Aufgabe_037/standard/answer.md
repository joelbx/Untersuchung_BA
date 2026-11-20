Fixed the undefined-variable error in YAML templates. `AnsibleDumper` now triggers Jinja’s undefined error for `AnsibleUndefined`; `to_yaml` and `to_nice_yaml` report filter-specific failures while preserving the original exception. The templating layer surfaces those failures as `AnsibleUndefinedVariable`.

Verification: 64 relevant unit tests passed.