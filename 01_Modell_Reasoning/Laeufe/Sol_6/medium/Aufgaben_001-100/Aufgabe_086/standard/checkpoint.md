Task: Add destination_ports support to iptables module.
Status: Complete.
Changes: Documented and registered destination_ports as a list of strings with default []; build -m multiport --dports via append_match and append_csv; validate tcp/udp/udplite/dccp/sctp; added example and unit coverage for supported/unsupported protocols and explicit multiport match.
Verification: PYTHONPATH=/app/lib:/app/test/lib python -m pytest -q test/units/modules/test_iptables.py (24 passed); git diff --check passed.
