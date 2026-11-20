Updated the repository to require **Python 3.12 or newer on the controller**. Ansible and ansible-test now show the same version error; package metadata, controller test versions, and the changelog reflect the change.

Collection extraction now passes `dirname` unchanged to `tar.getmember()` and no longer uses the private TarFile cache. I also removed controller compatibility branches for older Python versions.

Verification: 80 relevant tests passed, 1 skipped; both entry points produced identical errors on Python 3.11. The tests used a simulated 3.12 version because this workspace has no native Python 3.12 interpreter.