Added `LinuxHardware.get_sysinfo_facts()` to read IBM Z hardware identifiers from `/proc/sysinfo` and include them in gathered facts. It returns `{}` when the file is absent, keeps undiscovered fields as `NA`, and removes leading zeros from the serial.

The relevant facts and hardware tests passed: **111 passed, 5 skipped**. `git diff --check` passed. No delegation was used.