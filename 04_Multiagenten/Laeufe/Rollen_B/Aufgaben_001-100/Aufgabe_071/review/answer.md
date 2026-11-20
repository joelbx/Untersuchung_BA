VERDICT: ACCEPT

I found no correctness or regression issue in the applied CLIXML patch.

- `python -m pytest -q test/units/plugins/shell/test_powershell.py` — 10 passed.
- `python -m pytest -q test/units/plugins/shell` — 15 passed.

TEST_ENVIRONMENT_PROBLEM: none. I made no project code or test changes.