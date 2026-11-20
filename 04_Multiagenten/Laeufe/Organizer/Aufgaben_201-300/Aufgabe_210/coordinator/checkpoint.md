# Checkpoint

Issue: Avoid duplicate loop and delegate_to evaluation in TaskExecutor.
Status: implementation complete; focused tests and delegation integration playbooks pass.
Changes: TaskExecutor receives VariableManager, evaluates loop items once, resolves delegation before iterations (including item-dependent targets), and removes loop cache use. VariableManager exposes get_delegated_vars_and_hostname and defaults get_vars to no delegation. Task exposes get_play through parent blocks. Legacy delegation method is deprecated.
Tests: 36 focused unit tests passed; test_delegate_to_loop_randomness.yml, test_delegate_to_loop_caching.yml, and test_delegate_to_lookup_context.yml passed.
Delegation: none used.
