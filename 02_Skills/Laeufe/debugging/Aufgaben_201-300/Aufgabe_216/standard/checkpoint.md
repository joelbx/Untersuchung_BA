# SSH connection issue checkpoint

Status: investigating root cause before edits.

Constraints: local repository only; no downloads; preserve git history and index.

Tool note: `rg` is unavailable (`/bin/bash: rg: command not found`); use grep/find.

Root cause: SSH plugin documentation declares options, but runtime reads C constants and PlayContext directly for retries, batch mode, transfer method, SCP selection, identity/user/timeout, and control path. Config manager precedence only applies through get_option. Reset checks for a bare `ControlPath=` element and may skip the actual `-o ControlPath=...` socket. CLI SSH extra args live in PlayContext but are not passed to plugin option resolution.

Hypothesis: move those runtime reads to get_option, bridge explicit CLI extras through set_options task keys, and inspect the effective ControlPath argument when resetting. Validate with failing tests first.

Check attempt: `PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/plugins/connection/test_ssh.py test/units/plugins/connection/test_ssh_options_regression.py test/units/playbook/test_play_context.py test/units/utils/test_ssh_functions.py` failed with exit code 4: `ERROR: file or directory not found: test/units/utils/test_ssh_functions.py`. No tests ran; rerun with existing paths.

Implementation: SSH runtime now consumes get_option for arguments, executable, identity, user, timeout, retries, transfer method, batch mode, SCP preference, host key checking, and control path. CLI SSH arguments and authentication fields are bridged into plugin set_options so normal precedence applies. Reset sends `ssh -O check` with the effective command options and only sends `-O stop` if the check succeeds; otherwise it emits a debug message. SSH-specific core config definitions were removed. PlayContext and smart transport selection no longer require those constants.

Verification: `PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/plugins/connection/test_ssh.py test/units/plugins/connection/test_ssh_options_regression.py test/units/playbook/test_play_context.py test/units/executor/test_task_executor.py` passed (39 tests). `git diff --check` passed. Direct `PlayContext` smart transport smoke check returned `ssh`.

Earlier check failure: `PYTHONPATH=lib python - <<'PY' ... C.config.get_config_value('ssh_executable', plugin_type='connection', plugin_name='ssh') ... PY` raised `AnsibleError: Requested entry ... ssh_executable was not defined in configuration` because plugin definitions had not been registered. Fixed by loading the plugin before accessing its option; subsequent smart transport smoke check passed.
