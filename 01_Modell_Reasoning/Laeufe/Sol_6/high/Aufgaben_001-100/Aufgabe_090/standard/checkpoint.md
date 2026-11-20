Task: Resolve `/lists/add` POST failures caused by query/form parameter conflicts.
Status: Complete. Body forms are parsed with parse_qs and isolated from web.input; nested-field defaults are omitted, invalid seeds are ignored, and unflatten honors later assignments.
Verification: 18 focused pytest cases passed; ruff check and git diff --check passed.
Constraints: Edit checked-out files only; preserve git history/index and harness configuration; use local code and tests.
