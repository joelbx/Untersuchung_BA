Implemented the SSH option and reset changes.

- SSH command construction, retries, transfers, timeouts, and ControlPath handling now use plugin options. CLI values enter the normal option resolver.
- Reset checks the persistent master with the effective SSH parameters and stops it only when the check succeeds.
- Removed the duplicate SSH settings from core config and updated transport detection and existing unit fixtures.

Validation: `PYTHONPATH=lib python -m pytest -q test/units/playbook/test_play_context.py test/units/plugins/connection/test_ssh.py` — **20 passed**. `git diff --check` is clean.

See [ssh.py](/app/lib/ansible/plugins/connection/ssh.py) and [checkpoint.md](/app/.codex-role-output/checkpoint.md).