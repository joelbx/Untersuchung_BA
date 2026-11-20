# Checkpoint

Task: resolve pip module fallback when the current interpreter has the pip library but no pip executable is found.

Plan: inspect the module and focused existing tests; implement interpreter-bound launcher, pip detection, package listing fallback, and virtualenv path handling; run relevant existing tests.
