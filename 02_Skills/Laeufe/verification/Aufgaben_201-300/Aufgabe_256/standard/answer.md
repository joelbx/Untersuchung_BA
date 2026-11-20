Updated [Play](/app/lib/ansible/playbook/play.py:100) so `load` leaves `name` untouched, `get_name` derives it from the current hosts, and `_validate_hosts` raises parser errors for invalid values only when `hosts` was supplied. Added coverage in [test_play.py](/app/test/units/playbook/test_play.py:38).

Verification: all 247 playbook unit tests passed. A CLI check of an invalid host value produced the intended parser error with a source location, rather than an unexpected exception.

This checkout has `is_sequence` in `ansible.module_utils.common.collections`, not `ansible.utils.collection_loader`, so the fix uses the existing helper.