Fixed the YAML filters so an `AnsibleUndefined` value surfaces Jinja’s undefined-variable error instead of PyYAML’s `RepresenterError`. `to_yaml` and `to_nice_yaml` now raise `AnsibleFilterError` with the filter name and preserve the original exception.

Added regression tests for nested undefined values and ordinary values. The relevant existing test suites pass: **16 tests**.