# Checkpoint

Task: fix Linux hardware facts for IBM Z / s390 using `/proc/sysinfo`.

Root cause: `LinuxHardware.populate()` only merges `get_dmi_facts()` for these fields. Its fallback fills all DMI fields with `NA` when `dmidecode` is absent. No `/proc/sysinfo` reader exists. The existing `get_file_lines()` helper handles unreadable files and splits lines.

Pattern: CPU collection already handles s390x separately; hardware collection merges source dictionaries in `populate()`. Add a focused parser and merge its facts after DMI, so the existing behavior applies when `/proc/sysinfo` is absent.

Hypothesis: parsing the three `/proc/sysinfo` labels and merging its result after DMI will populate s390 facts while preserving other Linux behavior. Regression tests will exercise absent, present, and collection cases before the fix.

Reproduction: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware/test_linux.py -k 'Sysinfo'` failed in four tests because `get_sysinfo_facts` was absent (exit 1).

Fix: `get_sysinfo_facts()` reads `/proc/sysinfo` when present, returns exactly five hardware fields with `NA` defaults, parses Manufacturer/Type/Sequence Code, and removes leading zeros from the serial. `populate()` merges those fields after DMI facts.

Verification: `PYTHONPATH=lib python -m pytest -q -o reruns=0 test/units/module_utils/facts/hardware/test_linux.py` passed (15 tests, exit 0). `PYTHONPATH=lib python -m pytest -q -o reruns=0 test/units/module_utils/facts/hardware` passed (21 tests, exit 0). `git diff --check` passed (exit 0).
