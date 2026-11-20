Updated `QtColor` to scale HSV/HSVA hue percentages to 359 while keeping the other channels at 255. The parser now validates the function name and component count before converting values. Added regression tests for percentage boundaries and invalid inputs.

Verification: all 36 focused `QtColor` tests pass; `git diff --check` passes.