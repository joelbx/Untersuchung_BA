# WinRM kinit fix checkpoint

Resolved the WinRM Kerberos kinit argument issue. `rg` was unavailable (`/bin/bash: rg: command not found`), so repository discovery used `find` and `grep`.

## Status

- Added `kinit_args` as `ansible_winrm_kinit_args` and parsed it into argument tokens.
- Parsed existing `kinit_cmd` values with embedded arguments for compatibility with the reported configuration.
- Kept delegation's `-f` only when `kinit_args` is absent. Both execution paths use the same command tokens, and each call creates a fresh credential cache.
- Added unit coverage for command arguments, delegation precedence, one invocation per attempt, and unique cache paths.

## Verification

- `python -m pytest test/units/plugins/connection/test_winrm.py -q`: 36 passed.
- `git diff --check`: passed.
