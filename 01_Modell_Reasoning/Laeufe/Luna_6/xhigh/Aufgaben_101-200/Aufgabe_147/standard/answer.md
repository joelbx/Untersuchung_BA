Updated [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts) to keep persisted fields in one config object, expose `Version` and `LocalStorageKey`, and accept explicit version and storage parameters. Loading now avoids writes for current-version configs with a signup token; migrations and token generation write the underscored config keys, with credentials stored by user ID and restored as a `Map`.

Invalid JSON and unavailable storage recover without throwing. Migration preserves credential data and is idempotent. The checkpoint is in `.codex-role-output/checkpoint.md`.

Verification passed: `npm run types` and the client suite (3,050 assertions).