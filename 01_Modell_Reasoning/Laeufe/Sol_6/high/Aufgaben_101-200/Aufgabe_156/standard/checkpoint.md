# Checkpoint

Task: implement predictable no_log value and key sanitization in `basic.py`, integrate key sanitization in `uri`, and run relevant existing tests.

Status: implemented iterative value and key sanitization, wired `uri` key filtering,
and preserved date serialization at the JSON boundary. Added focused tests.

Validation: 34 focused tests pass. `git diff --check` passes. The full basic
directory has 22 failures from warning/deprecation state shared between test
files; those failures are unrelated to the sanitization changes. A small
test selection reproduces the warning-state leak.
