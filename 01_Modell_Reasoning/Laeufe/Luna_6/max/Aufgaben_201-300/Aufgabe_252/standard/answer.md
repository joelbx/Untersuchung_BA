Implemented the sysctl parser updates in [sysctl.py](/app/lib/ansible/module_utils/facts/sysctl.py:22): it supports `=`, `:`, and space delimiters, preserves continuation line breaks, and warns while continuing past malformed lines. Command failures warn and return an empty dictionary.

Updated [openbsd.py](/app/lib/ansible/module_utils/facts/hardware/openbsd.py:122) to run `sysctl -n kern.boottime` and calculate uptime only from numeric output. Missing sysctl raises `ValueError`; nonzero status or invalid output omits the fact.

**Verification:** Targeted tests passed (92 passed, 5 skipped). The full facts suite had one timing failure; that test passed when rerun alone. `git diff --check` passed.