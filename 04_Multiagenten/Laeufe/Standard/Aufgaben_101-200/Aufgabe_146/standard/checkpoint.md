Task: Fix Linux hardware facts on IBM Z / s390 by reading /proc/sysinfo.
Status: Implemented get_sysinfo_facts and merged its values into Linux hardware facts after DMI facts. Added parser and collection tests.
Verification: 18 relevant unit tests passed; git diff --check passed.
