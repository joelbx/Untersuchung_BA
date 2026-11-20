Implemented host validation and dynamic play naming in [play.py](/app/lib/ansible/playbook/play.py). Added coverage for invalid host values, omitted hosts, and derived names in [test_play.py](/app/test/units/playbook/test_play.py).

The focused Play unit suite passed: 13 tests. `git diff --check` passed.

This checkout does not export `is_sequence` from `ansible.utils.collection_loader`; the implementation uses the available `ansible.module_utils.common.collections.is_sequence` helper.