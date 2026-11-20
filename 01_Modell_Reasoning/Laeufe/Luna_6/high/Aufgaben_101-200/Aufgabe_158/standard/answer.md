Implemented ZIP timestamp validation in [unarchive.py](/app/lib/ansible/modules/unarchive.py). Invalid dates and years outside 1980–2107 now fall back to the ZIP epoch, and `is_unarchived` uses the validated timestamp.

Verification: `pytest -q test/units/modules/test_unarchive.py` passed (3 tests); `git diff --check` passed. Checkpoint saved to `.codex-role-output/checkpoint.md`.