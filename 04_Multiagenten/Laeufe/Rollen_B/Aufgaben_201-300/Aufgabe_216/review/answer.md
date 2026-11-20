VERDICT: FIX

**Code defects**

- [play_context.py](/app/lib/ansible/playbook/play_context.py:106) now defaults `ssh_executable` to `None`, but its smart transport selector still probes that value at line 397. The probe converts it to `b'None'` and reports ControlPersist unavailable, which can incorrectly select Paramiko when installed. Resolve the configured SSH executable before probing.
- [ssh.py](/app/lib/ansible/plugins/connection/ssh.py:521) drops an explicit CLI timeout when it equals `C.DEFAULT_TIMEOUT`, allowing a different `ssh_connection` timeout to override it. Track whether the CLI value was supplied instead of comparing values.

**Tests run**

- `PYTHONPATH=lib python -m pytest -q test/units/plugins/connection/test_ssh.py` — 22 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/playbook/test_play_context.py` — 2 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/config/test_data.py test/units/config/test_manager.py` — 62 passed.

**TEST_ENVIRONMENT_PROBLEM:** `PYTHONPATH=lib python -m pytest -q test/units/config` produced 68 passed and 8 setup errors. The existing [fixture](/app/test/units/config/manager/test_find_ini_config_file.py:38) assigns `None` to `os.environ['ANSIBLE_CONFIG']`; it should unset the variable for that case.