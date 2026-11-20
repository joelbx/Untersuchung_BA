VERDICT: FIX

The existing PowerShell and SSH tests pass: `PYTHONPATH=lib python -m pytest -q test/units/plugins/shell/test_powershell.py test/units/plugins/connection/test_ssh.py` → **46 passed**.

A correctness defect remains in [powershell.py](/app/lib/ansible/plugins/shell/powershell.py:122): the helper groups adjacent `<Objs>` elements before parsing. I reproduced a valid element followed by a malformed closed element; the helper returned the entire raw CLIXML input, losing the valid element’s decoded text. Parse adjacent elements separately so the valid text is replaced and the malformed element stays unchanged.

**TEST_ENVIRONMENT_PROBLEM:** None.