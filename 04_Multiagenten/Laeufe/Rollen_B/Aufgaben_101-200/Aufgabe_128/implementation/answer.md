Added `match_set` and `match_set_flags` to the iptables module. They must be supplied together, flags are limited to the four supported values, and rule construction emits the set clause with or without an explicit `match: ['set']`. A `!` prefix on the set name inverts the match.

The iptables unit tests pass (26 passed), and `git diff --check` is clean.