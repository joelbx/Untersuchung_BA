# Checkpoint

Resolved the `/lists/add` parameter precedence and unflattening issue. `ListRecord.from_input()` now parses nonempty URL-encoded bodies independently from query input, takes the first value for repeated fields, applies defaults only where no body field or nested descendant supplies a value, and filters invalid seed entries. Empty bodies continue through `web.input()` with the required defaults. `unflatten()` now lets the last assignment to a simple key win.

Verification: 21 relevant pytest tests passed; Ruff and `git diff --check` passed. No git history, index baseline, or harness configuration was changed.
