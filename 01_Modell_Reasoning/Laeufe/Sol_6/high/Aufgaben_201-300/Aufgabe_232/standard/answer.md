Implemented OS EOL lookup with the specified release dates, boundary-aware support checks, and per-target scan warnings. The scan summary now prints each warning with the required `Warning: ` prefix in evaluation order. Major version parsing is shared across components.

The relevant package tests passed with downloads disabled, and `git diff --check` passed.