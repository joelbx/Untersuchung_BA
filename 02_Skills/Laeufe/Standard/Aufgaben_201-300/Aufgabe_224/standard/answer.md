Moved the color interpolation helpers to `qtutils.py` and updated the download and tab progress indicators to use them. Interpolation still supports RGB, HSV, and HSL; the no-gradient path now rejects percentages outside 0–100 and preserves the start color’s spec.

Verification: 338 relevant tests passed, including the relocated interpolation tests. `git diff --check` passed.