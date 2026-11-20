Implemented ipset matching support in [iptables.py](/app/lib/ansible/modules/iptables.py). The module now accepts paired `match_set` and `match_set_flags` options, validates the four requested flag values, adds the `set` match automatically or uses an explicitly requested one, and supports inversion with `!`.

Added coverage in [test_iptables.py](/app/test/units/modules/test_iptables.py) for implicit and explicit set matches, inversion, common rule options, and incomplete parameter pairs.

Verification passed: `python -m pytest test/units/modules/test_iptables.py -q` (25 tests) and `git diff --check`.