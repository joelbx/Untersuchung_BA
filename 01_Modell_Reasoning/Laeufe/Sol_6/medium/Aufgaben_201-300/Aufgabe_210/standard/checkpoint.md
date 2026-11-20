Task: Resolve duplicate loop and delegate_to evaluation in TaskExecutor.
Status: Complete. TaskExecutor resolves fixed delegation before loop evaluation; item-dependent delegation is precomputed from the single loop item evaluation before iterations execute. VariableManager exposes get_delegated_vars_and_hostname; Task exposes get_play. Removed delegation from get_vars and loop cache workaround.
Verification: 35 focused unit tests passed. Existing delegation integration playbooks test_delegate_to_loop_caching.yml, test_delegate_to_loop_randomness.yml, resolve_vars.yml, and test_delegate_to_lookup_context.yml passed. git diff --check passed.
Constraints observed: local code/tests only; git history, index baseline, and harness configuration unchanged.
