# Checkpoint

Task: resolve SSH connection plugin option-source consistency and persistent reset detection in `/app`.

Implemented:
- SSH execution, transfer selection, retries, keys/users/timeouts, executables, and ControlPath settings now use connection plugin options.
- CLI connection arguments are fed into plugin option resolution, with inventory variables retaining the resolver's normal precedence.
- Persistent reset probes the master with the same effective SSH command parameters and issues `-O stop` only when `-O check` succeeds.
- Removed the duplicated SSH-only settings from `lib/ansible/config/base.yml`; transport autodetection now resolves the executable through the SSH plugin.
- Updated existing SSH unit fixtures to configure plugin options instead of removed global constants.

Validation:
- `PYTHONPATH=lib python -m pytest -q test/units/playbook/test_play_context.py test/units/plugins/connection/test_ssh.py` — 20 passed.
- `git diff --check` — clean.

Constraints observed: no network research/downloads/delegation; no history, index-baseline, or harness changes.
