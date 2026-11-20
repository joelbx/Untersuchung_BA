# Checkpoint

Implemented SSH option resolution in the connection plugin, transfer method selection, effective ControlPath generation, and reset via SSH `-O check` before `-O stop`. Removed SSH-specific core configuration definitions and adjusted smart transport lookup to load the plugin's executable setting.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py` passed (28 tests). `git diff --check` and `PYTHONPATH=lib python -m compileall -q lib/ansible/plugins/connection/ssh.py lib/ansible/utils/ssh_functions.py lib/ansible/playbook/play_context.py` exited 0. A local config manager lookup of `[ssh_connection]` values returned `-o ProxyJump=config` and `scp`.

Broader check: `PYTHONPATH=lib python -m pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py test/units/config/manager` had 33 passes and 8 setup errors. The config manager fixture `test/units/config/manager/test_find_ini_config_file.py:38` assigns `None` to `os.environ['ANSIBLE_CONFIG']`, causing `TypeError: str expected, not NoneType`. Those config manager cases remain unverified; the error occurs before their test bodies.

The first SSH test run without `PYTHONPATH=lib` imported the installed package rather than the checkout, so it was not used as verification.
