Added `destination_ports` as a list with an empty default. Rules now use the iptables `multiport` match and comma-separated `--dports` values; nonempty lists require `tcp`, `udp`, `udplite`, `dccp`, or `sctp`.

Added unit coverage for port lists, ranges, and unsupported protocols in [test_iptables.py](/app/test/units/modules/test_iptables.py).

Verification passed: `PYTHONPATH=/app/lib:/app/test python -m pytest test/units/modules/test_iptables.py -q` — 23 tests. The `ansible-test` wrapper could not run because its Python 3.8 environment lacks pytest. Checkpoint recorded in `.codex-role-output/checkpoint.md`.