# Checkpoint

Task: Fix CLIXML decoding in the Ansible PowerShell shell plugin according to the issue requirements.

Implemented in `lib/ansible/plugins/shell/powershell.py`:
- Added the requested `_parse_clixml(data: bytes, stream: str = "Error") -> bytes` annotations.
- Processes ordered `<Objs>` blocks, filters direct `<S>` elements by stream, joins their decoded text within a block, and separates nonempty block results with CRLF.
- Decodes hexadecimal UTF-16 code unit escapes, combines valid surrogate pairs, handles the canonical `_x005F_` escape, preserves control characters and unpaired surrogates, and leaves malformed escapes untouched.
- Returns UTF-8 bytes with `surrogatepass`.

Regression coverage added in `test/units/plugins/shell/test_powershell.py`.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/plugins/shell/test_powershell.py` passed (9 tests); `git diff --check` passed.
