# Checkpoint

Task: make YAML dumping of AnsibleUndefined raise an undefined-variable error, and have to_yaml/to_nice_yaml wrap failures with filter-specific AnsibleFilterError messages.

Status: complete.

Changes:
- AnsibleDumper represents AnsibleUndefined by evaluating its truth value, surfacing Jinja's UndefinedError.
- to_yaml and to_nice_yaml wrap failures in filter-specific AnsibleFilterError values and retain the original exception.
- Templar converts filter errors caused by UndefinedError into AnsibleUndefinedVariable while retaining the filter error and its cause.
- Added regression coverage for direct YAML dumping, both filters, and template rendering.

Verification: 164 YAML, filter, and template unit tests passed. One existing constructor test was deselected because this environment lacks the mocker fixture; the full run otherwise passed 164 tests and failed at that test's setup. git diff --check passed.
