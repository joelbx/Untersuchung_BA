Fixed `Play` so it derives a name from `hosts` when needed without changing the input data. Invalid `hosts` values now raise the specified `AnsibleParserError` messages instead of an unexpected exception.

Added unit tests for validation and name derivation. All 248 playbook unit tests pass; `git diff --check` passes.