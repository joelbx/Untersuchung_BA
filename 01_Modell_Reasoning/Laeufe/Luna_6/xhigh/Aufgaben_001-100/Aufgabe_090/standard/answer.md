Implemented the `/lists/add` input fix. Nonempty request bodies are parsed independently with `parse_qs` and first-value semantics; defaults no longer block nested body fields. Seed parsing skips malformed or empty entries, and unflattening now gives later assignments precedence.

Added regression tests. The relevant suites passed: **17 passed**. `git diff --check` passed.