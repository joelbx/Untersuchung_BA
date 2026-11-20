# Checkpoint

Task: Decode embedded CLIXML in Windows SSH stderr while preserving unrelated and malformed bytes.

Status: Complete. Added a line-scanning stderr CLIXML replacement helper in the SSH plugin, wired it into Windows command execution, and corrected the UTF-16-BE escape regex in the PowerShell parser. Added regression coverage for surrounding bytes, multiple and multiline blocks, cp437 fallback, malformed data, and Unicode lookalikes.

Verification: `pytest -q test/units/plugins/connection/test_ssh.py test/units/plugins/shell/test_powershell.py` passed (52 tests); `git diff --check` passed.
