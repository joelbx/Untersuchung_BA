# Checkpoint

Issue: storage backend polling goroutines need explicit lifecycle management.

Findings: `Poller.Poll(ctx, update)` currently owns no context or completion signal; Git, local, OCI, S3, and Azure Blob each start it in a goroutine and discard its handle. Plan: make `Poller` own a derived context, callback, and done channel; have `Close` cancel and wait; retain poller pointers in each polling SnapshotStore and expose idempotent `Close() error` (nil poller is a no-op). Keep Git's immutable hash source without a poller.
