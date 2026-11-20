Updated TaskExecutor to resolve `delegate_to` once before evaluating loop items. VariableManager now provides `get_delegated_vars_and_hostname()`, Task exposes `get_play()` through its parent blocks, and the loop evaluation cache has been removed. Variable retrieval no longer resolves delegation by default.

Verification: 372 unit tests passed, 1 skipped; `git diff --check` passed.