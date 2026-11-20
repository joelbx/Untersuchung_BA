# Checkpoint

Task: Fix the password lookup plugin's term parameter handling, option defaults, and character parsing.

Status: Implemented instance-based parameter parsing in `LookupModule`. Inline values override plugin options; `chars` accepts a list or comma-separated string while preserving literal commas. The working tree was clean before edits.

Verification: `test/units/plugins/lookup/test_password.py` passed (34 tests). The existing `lookup_password` integration playbook passed (31 tasks) when run directly without its dependency-installing wrapper. `git diff --check` passed.
