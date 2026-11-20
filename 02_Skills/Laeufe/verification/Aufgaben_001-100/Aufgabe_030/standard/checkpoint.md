# Checkpoint

Task: Correct AIX processor facts in the checked-out repository.

Changes: AIX CPU facts now report one processor, count available devices as cores, default SMT threads to one, derive vCPUs, and return the CPU type in a list. Added unit coverage for SMT, missing SMT, and no available processor.

Verification:
- `python -m pytest -q test/units/module_utils/facts/hardware/test_aix.py`: initially failed for both regression cases against the old implementation.
- `python -m pytest -q test/units/module_utils/facts/hardware`: 18 passed.
- `git diff --check`: exit 0.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
