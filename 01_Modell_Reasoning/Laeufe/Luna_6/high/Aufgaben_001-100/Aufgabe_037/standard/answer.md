Implemented undefined handling for YAML dumping:

- Added an `AnsibleUndefined` representer that triggers Jinja’s undefined-variable error during serialization.
- Updated `to_yaml` and `to_nice_yaml` to raise filter-specific `AnsibleFilterError`s while preserving the original exception as the cause.

The existing relevant unit suites passed: **11 passed**. A direct check confirmed both filters report the undefined variable and retain a chained `UndefinedError`. `git diff --check` passed.