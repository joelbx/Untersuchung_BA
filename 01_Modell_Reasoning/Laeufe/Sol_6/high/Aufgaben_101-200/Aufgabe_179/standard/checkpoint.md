# RemoteCluster status and heartbeat fix

Completed repository edits. Presence declares UpdateRemoteCluster; local storage serializes and writes the resource with its expiry. Auth status refresh persists changed status and keeps the maximum heartbeat in UTC, including after tunnel removal. Auth wrappers implement the expanded interface. Added regression tests for create, update, partial deletion, final deletion, persistence, and expiry.

Verification: focused auth and local regression tests passed; existing remote cluster and tunnel CRUD tests passed; cache and service packages compiled; git diff --check passed.
