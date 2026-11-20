Task: Fix SSH connection option resolution and persistent reset detection.
Status: Implemented and verified.
Changes: SSH plugin uses resolved get_option values for command construction, retries, transfer selection, and reset. CLI arguments are fed to plugin option resolution. Removed duplicate SSH-specific core settings and updated remaining consumers. Reset probes active socket with the effective command before stop. Added and updated SSH unit tests.
Verification: PYTHONPATH=/app/lib python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py (25 passed). git diff --check passed.
Delegation: None.
