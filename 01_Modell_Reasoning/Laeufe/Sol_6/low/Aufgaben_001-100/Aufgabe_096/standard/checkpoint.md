Task: Fix atomic_move default permissions and warnings in module_utils.
Status: implemented and verified.
Changes: _DEFAULT_PERM=0600; track created paths when mode is accepted but omitted; emit exact warning during result formatting; clear tracked path on explicit set_mode_if_different. Added focused tests and corrected existing expectations for preserving an existing file's mode.
Verification: PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py (45 passed).
