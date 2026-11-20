# Checkpoint

Task: Resolve SSH option precedence and persistent reset detection.
Status: Complete.
Changes: SSH-specific core config entries removed and resolved by the SSH plugin. Command construction, transfers, retries, and control socket reset use get_option values. CLI connection arguments are fed into plugin option resolution beneath inventory variables. Reset checks the configured master with `ssh -O check` and only sends `stop` when it succeeds. ControlPath expansion preserves SSH tokens.
Verification: `PYTHONPATH=lib python -m pytest test/units/plugins/connection test/units/playbook/test_play_context.py -q` passed (68 tests). `git diff --check` passed.
