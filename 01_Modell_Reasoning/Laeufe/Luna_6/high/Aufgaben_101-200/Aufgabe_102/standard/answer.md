Added the Linux `locally_reachable_ips` fact with sorted, de-duplicated IPv4 and IPv6 addresses and prefixes from routes marked `scope host`. Missing commands or query failures return empty lists and emit a concise warning. Registered the fact and added focused unit tests.

Validation: 98 passed, 5 skipped; `git diff --check` passed. `ansible-test units` could not start because pytest is missing its `--forked` and `-n` plugins; direct pytest passed.

Updated `.codex-role-output/checkpoint.md`.