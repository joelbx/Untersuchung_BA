# Checkpoint

Task: resolve SSH connection plugin configuration precedence and persistent socket reset behavior.

Inspection found SSH runtime reads from global constants and PlayContext fields, while plugin metadata omitted `timeout` and `transfer_method`. The SSH plugin now owns these option definitions and resolves CLI values through `set_options`; persistent reset checks the active master using the same built SSH arguments. Global SSH-only config entries and PlayContext references to their generated constants have been removed.

Current status: implementation and regression tests are complete. The focused SSH, PlayContext, config manager, and CLI helper suites pass together: 118 passed. `git diff --check` and the retired-constant source scan are clean.
