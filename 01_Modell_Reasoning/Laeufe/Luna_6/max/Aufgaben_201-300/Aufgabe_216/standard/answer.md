Implemented SSH option resolution through the plugin’s `get_option()` flow, including CLI, config, environment, and inventory values. Removed the SSH-specific core config entries and updated transport selection to resolve the SSH executable through plugin configuration.

Reset now runs `ssh -O check` with the effective connection options and skips `-O stop` with a debug message when no master is active. Added regression coverage for option precedence, transfer selection, and reset behavior.

Validation: **118 tests passed** across the SSH, PlayContext, config manager, and CLI helper suites. `git diff --check` passed.