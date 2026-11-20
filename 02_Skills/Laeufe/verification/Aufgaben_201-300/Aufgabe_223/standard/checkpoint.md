# Checkpoint

Task: fix module shebang handling in /app.

Implemented: extract the source shebang before building new-style Python wrappers; resolve Python versioned interpreters using Python overrides; preserve unchanged source shebang text; add a default for modules without a shebang; insert the encoding line after source shebangs. Added focused coverage for versioned/custom interpreters, arguments, overrides, missing shebangs, and a shebang without a trailing newline.

Verification: `python -m pytest -q test/units/executor/module_common` exited 0 (54 passed, 1 warning from ZipFile finalization in an existing recursive-finder test). `git diff --check` exited 0.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.
