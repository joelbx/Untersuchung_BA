Task: Fix Linux hardware facts for IBM Z / s390 using /proc/sysinfo.
Status: Implemented get_sysinfo_facts and merged its values into populate. Added tests for absent, complete, and partial sysinfo data. Relevant existing tests passed (108 passed, 5 skipped). Next: final diff review.
