# Checkpoint

Implemented the SSH option ownership and runtime resolution changes.

- SSH plugin metadata now owns `transfer_method` and `timeout`, and runtime paths read effective plugin options for arguments, retry count, executable, key, remote user, control path settings, batch mode, and transfer selection.
- Removed the SSH-only global config entries from `lib/ansible/config/base.yml`; updated PlayContext and transport detection to no longer depend on those constants.
- Reset checks the effective command's ControlPersist/ControlPath settings and skips stopping when the socket path is absent, with a debug message.

Validation: `test/units/plugins/connection/test_ssh.py` and `test/units/playbook/test_play_context.py` pass (20 tests); `git diff --check` passes. Final review in progress.
