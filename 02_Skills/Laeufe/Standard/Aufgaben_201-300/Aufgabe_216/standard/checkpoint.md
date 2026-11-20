# SSH connection issue checkpoint

Status: implemented and verified.

Changes:
- SSH runtime reads plugin options for command arguments, authentication, timeout, retries, transfer method, batch mode, and control paths.
- CLI connection arguments are passed into plugin option resolution while inventory variables retain higher precedence.
- Reset issues an SSH multiplex `-O check` using the same effective command options, then issues `-O stop` only when a socket responds.
- Removed SSH-only core configuration definitions and their PlayContext defaults; smart transport detection resolves the SSH executable from the plugin.
- Updated existing SSH tests to set plugin options and added precedence, transfer method, and reset tests.

Checks:
- `PYTHONPATH=lib pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py`: 24 passed.
- `PYTHONPATH=lib pytest -q test/units/plugins/connection`: 66 passed.
- `git diff --check`: passed.

An attempted command, `PYTHONPATH=lib pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py test/units/utils/test_ssh_functions.py`, returned exit 4 because `test/units/utils/test_ssh_functions.py` does not exist. The existing SSH and play-context test paths were then run successfully. No download or external research was used.
