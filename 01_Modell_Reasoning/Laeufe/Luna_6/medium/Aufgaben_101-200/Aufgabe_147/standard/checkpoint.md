# DeviceConfig issue checkpoint

Implemented in `src/misc/DeviceConfig.ts`: persisted fields now live in a single config object; exact underscored keys are serialized; credentials deserialize to a Map and legacy arrays migrate by user ID; initialization writes only after migration, invalid/missing storage data, or signup token creation. Static Version and LocalStorageKey are exposed and the global instance passes both explicitly.

Verification: `npx tsc --noEmit --pretty false` passed. The client test runner is building but stalled compiling the repository's native `better-sqlite3` dependency; an earlier invocation from the wrong working directory failed to locate its builder. No repository tests have completed yet.
