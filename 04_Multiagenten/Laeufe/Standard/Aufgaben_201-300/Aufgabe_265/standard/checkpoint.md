# Checkpoint

Task: Correct `QtColor` percentage parsing for hue and validate color function names and component counts.

Status: Complete. `QtColor` now scales hue percentages to 359, other channels to 255, and validates color function names and arity before conversion. Added regression cases for HSV/HSVA, RGB/RGBA, and invalid functions/counts.

Verification: 54 tests passed in `TestQtColor` and `TestQssColor` with pytest's obsolete `--strict` option overridden. `git diff --check` and `compileall` passed.
