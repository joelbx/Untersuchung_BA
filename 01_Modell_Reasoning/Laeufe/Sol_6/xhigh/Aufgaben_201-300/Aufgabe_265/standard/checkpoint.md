# Checkpoint

Task: Correct percentage hue parsing and validate supported `QtColor` functions in `qutebrowser/config/configtypes.py`.

Status: Implemented and verified. Hue percentages use a 359 scale; RGB, saturation, value, and alpha use 255. Function names and component counts are validated before conversion.

Verification: `pytest -q -o addopts='' tests/unit/config/test_configtypes.py -k 'TestQtColor or TestQssColor'` passed (54 tests). `git diff --check` passed. The full config types test file produced 977 passes and 60 unrelated failures from Hypothesis fixture health checks and other pre-existing environment issues.
