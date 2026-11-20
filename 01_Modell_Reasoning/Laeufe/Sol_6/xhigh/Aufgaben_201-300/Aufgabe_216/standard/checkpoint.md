Task: resolve SSH connection option precedence and persistent reset detection.
Status: complete.
Changes: SSH plugin reads effective options with get_option for command construction, transfer selection, retries, timeout, and control paths. CLI values carried by PlayContext enter plugin option resolution as task keys. SSH-only definitions were removed from core config; related PlayContext and smart transport references were updated. Reset checks the control socket with the same resolved command options before sending stop.
Verification: PYTHONPATH=lib:test pytest -q test/units/config/test_manager.py test/units/executor/test_task_executor.py test/units/playbook/test_play_context.py test/units/plugins/connection/test_ssh.py — 96 passed. git diff --check passed.
