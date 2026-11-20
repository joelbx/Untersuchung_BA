Added the `locally_reachable_ips` fact to the Linux network collector, with sorted, deduplicated canonical IPv4 and IPv6 destinations. Query failures or empty results return empty lists with concise warnings. Registered the fact ID for subset selection.

Validation: 136 existing fact tests passed; 5 skipped. `git diff --check` passed. The `ansible-test` wrapper could not start because pytest’s `--forked` and `-n` plugins are unavailable, so I ran the existing suites directly with pytest.

Files: [linux.py](/app/lib/ansible/module_utils/facts/network/linux.py), [base.py](/app/lib/ansible/module_utils/facts/network/base.py).