# Polling lifecycle fix

Goal: make filesystem storage pollers stop and finish before their SnapshotStore closes.

Implemented: Poller owns a child context, starts its loop once, and Close cancels and waits. Git, local, S3, Azure Blob, and OCI snapshot stores retain their pollers and expose Close. The declarative Store wrapper forwards Close.

Verification: affected filesystem storage package tests passed after all edits. Focused race-enabled poller and wrapper tests passed. `git diff --check` passed.
