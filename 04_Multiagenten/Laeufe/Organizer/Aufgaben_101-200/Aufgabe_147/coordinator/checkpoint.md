# DeviceConfig issue checkpoint

- Initial repository status: clean.
- Located implementation in `src/misc/DeviceConfig.ts` and existing migration test in `test/client/misc/DeviceConfigTest.ts`.
- Current load writes during every successful parse before all fields are initialized, risking loss of saved fields. Current migration leaves credentials as an array.
- Plan: keep all persisted fields in one config object, migrate credentials to a keyed object, deserialize to Map, and write only on migration or signup token creation. Run relevant existing tests and type check.

## Completed
- Reworked DeviceConfig to hold the persisted schema in one config object and use explicit version/storage constructor parameters. Added public static Version and LocalStorageKey.
- Load now migrates old credential arrays to userId-keyed objects, restores credentials to a Map, fills defaults for known fields, and writes only after migration or token creation. Storage failures and invalid JSON recover to defaults.
- Added no-op guards for setters and credential storage, preserving existing database keys.
- Added DeviceConfig regression coverage for unchanged loads, migration/field preservation, missing token recovery, unavailable storage, and idempotence.
- Verification: `npm run testclient -- -c` passed all 3086 assertions; app and test TypeScript checks passed; `git diff --check` passed.
- No delegation used.
