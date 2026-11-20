# Checkpoint

- Objective: replace DynamoDB audit event JSON-string `Fields` storage with native `FieldsMap`, while retaining legacy reads and building resumable, batch-based, locked migration support.
- Initial status: repository is `/app`; working tree was clean before this checkpoint.
- Investigation found the DynamoDB event codec, existing RFD24 scan/batch migration, and `backend.RunWhileLocked`. Reads currently decode only `Fields`; writes occur through three paths.
- Implementation plan: add `backend.FlagKey`; write `FieldsMap`; decode either representation; migrate legacy rows with a locked, resumable scan and batch writes, persisting a per-table backend checkpoint after each fully written scan page.
- Implemented the exported flag key helper, native map encoding on all three write paths, dual-format readers, and automatic migration. The migration batches at 25 items, limits each scan page, retries unprocessed writes, validates JSON/map semantics, and checkpoints through the shared backend flags namespace while holding the existing migration lock.
- Added focused tests for flag key composition, native map encoding, empty nested maps/lists, semantic round trips, and legacy reads. Final verification passed: `go test ./lib/events/dynamoevents ./lib/backend`; `git diff --check` is clean.
- Constraints: use repository code and tests only; preserve git history, index baseline, and harness configuration.
