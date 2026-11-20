# Checkpoint

Issue: replace label/cache heuristics in `useShouldMoveOut` with validation of the active element ID against the supplied valid element IDs, suspending while loading.

Progress: locating the hook, its callers, and existing focused tests. Next: propagate the mailbox slice's IDs/loading state through both view components, update the hook, and run existing relevant tests.
