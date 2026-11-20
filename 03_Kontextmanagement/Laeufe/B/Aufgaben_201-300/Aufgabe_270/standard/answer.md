Resolved the public page session lookup. It now selects the latest valid persisted session as one object containing both UID and localID, and the public session and telemetry callers use it. I removed the `LAST_ACTIVE_PING` paths.

The lookup and telemetry tests pass (10 tests total). Type checking remains blocked by an OpenPGP type conflict in an untouched crypto package.