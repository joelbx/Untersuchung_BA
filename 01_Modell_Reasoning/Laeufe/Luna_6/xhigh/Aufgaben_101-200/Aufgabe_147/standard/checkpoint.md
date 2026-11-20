# Checkpoint

Task: fix DeviceConfig loading/migration so persisted settings are preserved and storage is written only for a migration or missing signup token.

Located `src/misc/DeviceConfig.ts` and its existing client test. The current `_load()` rewrites every valid config, persists the class instance itself, and does not key migrated credentials by user ID. No repository `AGENTS.md` files were found.

Implementation: persisted values now live in one `_config` object, with injectable schema version and storage. Load deserializes `_credentials` as a `Map`; writes serialize only `_config` and convert credentials to a user-ID keyed object. Current-version configs with a token do not trigger a load-time write. Older configs are migrated and written once; missing tokens are generated and written. Migration preserves extra credential properties and is idempotent.

Verification: `npm run types` passed. Existing client suite passed: 3,050 assertions (3,542 old-style total).
