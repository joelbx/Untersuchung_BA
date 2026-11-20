Task: Fix PowerShell CLIXML decoding in /app.
Status: Implemented stream filtering, per-block concatenation and separators, UTF-16 escape decoding (including surrogate pairs and escaped underscores), empty element handling, and surrogate-safe UTF-8 encoding. Updated focused tests.
Checks:
- `python -m pytest -q test/units/plugins/shell/test_powershell.py`: 14 passed.
- `python -m pytest -q test/units/plugins/shell && git diff --check`: 19 passed; diff check passed.
No offline tooling failures. `rg` is unavailable; used local grep/find for discovery.
