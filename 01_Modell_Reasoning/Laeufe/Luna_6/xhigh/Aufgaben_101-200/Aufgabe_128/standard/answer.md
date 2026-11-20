Implemented ipset matching in [iptables.py](/app/lib/ansible/modules/iptables.py). The module now validates `match_set` and `match_set_flags` as a pair, accepts the four specified flag values, adds `-m set` when needed, avoids duplicating an explicit set match, and supports inversion with a `!` prefix on the set name.

Added regression coverage in [test_iptables.py](/app/test/units/modules/test_iptables.py) for match construction, inversion, validation, and integration with ports, jumps, and comments.

Verification passed: **25 unit tests**, Python compilation, and `git diff --check`.