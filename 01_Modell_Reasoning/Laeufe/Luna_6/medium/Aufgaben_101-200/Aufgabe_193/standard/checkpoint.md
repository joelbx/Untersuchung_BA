# Checkpoint

Implemented changes in `lib/ansible/cli/galaxy.py`:
- Added `-r/--requirements-file` to role install (retaining `--role-file` compatibility).
- The implicit `ansible-galaxy install` path parses combined requirements and installs collections at the configured default collection location when the roles path is not customized.
- Explicit role installs log ignored collections at verbose level; implicit installs with a custom roles path warn that collections cannot be installed there.
- Collection installs report ignored roles at verbose level and announce collection installation; role installation announces its start and handles empty role lists.

Verification: `py_compile` and `git diff --check` pass. Existing `test/units/cli/test_galaxy.py` reports 103 passed and 4 failures, all asserting collection path warning call counts (expected one/zero, observed two/one). Investigating whether this behavior predates the change remains outstanding.
