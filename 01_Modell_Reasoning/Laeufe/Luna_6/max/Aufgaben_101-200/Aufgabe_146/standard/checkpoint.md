# Checkpoint

Task complete: added s390 hardware fact parsing from `/proc/sysinfo`.

Implementation in `lib/ansible/module_utils/facts/hardware/linux.py`:
- `LinuxHardware.get_sysinfo_facts` returns `{}` when the file is absent and otherwise returns the five requested keys, defaulting undiscovered facts to `NA`.
- Manufacturer, Type, and Sequence Code populate system vendor, product name, and serial; serial leading zeros are stripped.
- DMI collection uses discovered sysinfo values to fill facts that remain `NA`.

Validation:
- Focused existing pytest files: 14 passed.
- `git diff --check`: passed.
- `ansible-test units` could not run because pytest does not recognize the runner's `-n` option (pytest-xdist is unavailable); the same test files passed with pytest directly.
