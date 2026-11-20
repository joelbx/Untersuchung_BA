# Checkpoint

Implemented SSH option resolution through plugin `get_option()` for the requested runtime paths, moved SSH-specific configuration definitions out of core config, and aligned play-context defaults and SSH utility fallback with plugin-owned defaults.

Persistent reset now constructs its probe with the plugin's effective SSH command settings, checks the resulting ControlPath, logs and skips stop when no socket exists, and stops only when a socket is present.

Validation: `python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py` passed (20 tests); `git diff --check` passed.
