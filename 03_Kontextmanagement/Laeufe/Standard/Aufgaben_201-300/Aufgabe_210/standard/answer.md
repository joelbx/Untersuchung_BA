Updated TaskExecutor to resolve `delegate_to` once before evaluating loop items. VariableManager now provides `get_delegated_vars_and_hostname()`, Task exposes `get_play()`, and the loop evaluation cache has been removed. Delegation resolution in `get_vars()` is off by default and its legacy path is marked deprecated.

Verification: 36 relevant tests passed.