Fixed the undefined-variable error path. `AnsibleDumper` now triggers Jinja’s undefined error for `AnsibleUndefined`; both YAML filters report named `AnsibleFilterError` failures with the original cause preserved; and template rendering surfaces those failures as `AnsibleUndefinedVariable`. Supported YAML values retain their existing behavior.

The relevant tests passed: **65 passed**.