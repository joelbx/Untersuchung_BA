# Checkpoint
Resolved /lists/add form/query conflict by parsing nonempty request bodies independently, applying defaults without masking nested fields, filtering invalid seeds, and allowing later simple assignments to win.
Validation: 16 targeted pytest tests passed; ruff and git diff --check passed.
