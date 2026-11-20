Task: Resolve duplicate loop and delegate_to evaluation in TaskExecutor.
Status: Implemented and verified.
Changes: Worker passes VariableManager to TaskExecutor; executor resolves delegation once before loop items; VariableManager exposes get_delegated_vars_and_hostname, defaults get_vars away from delegation, and no longer evaluates or caches loops; Task.get_play traverses parent blocks.
Verification: 372 passed, 1 skipped in executor, playbook, and vars unit suites; git diff --check passed.
