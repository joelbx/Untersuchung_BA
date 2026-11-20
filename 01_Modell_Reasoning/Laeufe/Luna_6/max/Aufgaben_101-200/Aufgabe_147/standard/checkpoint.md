# DeviceConfig overwrite issue checkpoint

- Task: make configuration loading and migration non-destructive, using the required underscored persisted keys.
- Implemented in `src/misc/DeviceConfig.ts`: persisted values live in one config object; schema version and storage are injected; reads and writes use the exact underscored keys; credentials deserialize to a Map and serialize as a user ID keyed object; legacy arrays migrate idempotently; defaults and signup tokens are generated safely.
- Tests updated in `test/client/misc/DeviceConfigTest.ts` for no-write current loads, field preservation, migration, idempotence, token generation, invalid/unavailable storage, and database key retention.
- Verification: `npm run types` passed; `npm run testclient` passed all 3,074 assertions; `git diff --check` passed.
