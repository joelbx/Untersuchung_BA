Fixed ZIP timestamp handling in [unarchive.py](/app/lib/ansible/modules/unarchive.py). The new `_valid_time_stamp` method extracts date components with a regex, accepts ZIP years 1980–2107, and uses the required 1980 epoch tuple for invalid dates. `is_unarchived` now uses that validated value.

The regression test reproduced the reported `ValueError` before the call-site fix. All 10 [unarchive unit tests](/app/test/units/modules/test_unarchive.py) now pass.

Broader verification remains incomplete: bare `pytest` stops while collecting an integration script, and the unit suite’s first failure is the unrelated `test_execute_list_collection_no_valid_paths`. Details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).