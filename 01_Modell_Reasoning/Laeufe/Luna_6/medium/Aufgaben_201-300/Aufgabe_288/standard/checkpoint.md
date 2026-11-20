# Checkpoint

Task: replace label/cache-driven move-out behavior with ID membership validation for conversation and message views.

Plan:
1. Locate the hook, mailbox container, and view props.
2. Propagate valid element IDs and loading state, deriving the active ID using `isAlwaysMessageLabels`.
3. Run relevant existing tests and report results.
