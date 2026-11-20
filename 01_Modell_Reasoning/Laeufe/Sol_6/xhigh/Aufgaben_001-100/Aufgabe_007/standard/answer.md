Updated the [WinRM connection plugin](/app/lib/ansible/plugins/connection/winrm.py) to support `ansible_winrm_kinit_args`. Both subprocess and pexpect now receive the same parsed command arguments. Custom arguments replace the default delegation `-f` flag; when no custom arguments are set, delegation still adds `-f`.

For the reported command, set `ansible_winrm_kinit_cmd: /opt/CA/uxauth/bin/uxconsole` and `ansible_winrm_kinit_args: '-krb -init'`. The [documentation](/app/docs/docsite/rst/user_guide/windows_winrm.rst) and [unit tests](/app/test/units/plugins/connection/test_winrm.py) cover this usage, both execution paths, and unique credential caches per attempt.

Verification: 35 WinRM unit tests passed; `git diff --check` passed.