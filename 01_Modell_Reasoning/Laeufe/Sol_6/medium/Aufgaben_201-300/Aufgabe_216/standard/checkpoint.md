Task: Resolve SSH connection option precedence and persistent reset detection.
Status: completed.
Changes: SSH runtime paths use plugin get_option; moved SSH-specific core settings into plugin; reset checks the live socket with the effective SSH command before stop; updated and added SSH tests.
Verification: PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py (23 passed); git diff --check.
