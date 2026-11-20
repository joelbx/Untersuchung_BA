# Checkpoint

Task: add IBM Z `/proc/sysinfo` hardware facts to Linux setup facts.

Status: implemented `LinuxHardware.get_sysinfo_facts()` and connected it to DMI facts. Added four tests covering missing file, parsing, missing fields, and DMI fallback. All four failed for the expected missing behavior before the implementation and then passed.

Tooling: `rg` is unavailable (`/bin/bash: line 1: rg: command not found`); using local alternatives.

Verification:

- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware`: 21 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts`: 409 passed, 5 skipped, 1 unrelated failure in `test/units/module_utils/facts/test_timeout.py::test_implicit_file_default_timesout` (expected timeout, returned `Succeeded after 2 sec`).
- `PYTHONPATH=lib python -m pytest -q`: collected 3824 items with 22 collection errors, then was interrupted while running integration targets; process exited 137. The full suite did not complete, so its remaining status is unknown.
