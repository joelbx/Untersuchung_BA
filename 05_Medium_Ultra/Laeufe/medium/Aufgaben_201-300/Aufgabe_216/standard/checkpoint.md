# SSH connection option and reset fix

Status: complete.

Changes: SSH runtime behavior now reads plugin options through `get_option()`; added `transfer_method` and `timeout` definitions; removed SSH-specific core definitions; preserved CLI options through plugin resolution; reset verifies the effective socket path before stopping; smart transport checks the resolved SSH executable.

Verification: 35 existing and added unit tests passed across SSH connection, PlayContext, and TaskExecutor. `git diff --check` passed.
