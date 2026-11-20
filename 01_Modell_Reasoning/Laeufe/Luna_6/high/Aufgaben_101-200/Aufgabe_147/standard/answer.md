Implemented the DeviceConfig persistence changes in [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts).

Loading now preserves the underscored config fields, deserializes credentials into a `Map`, migrates v2 credential arrays to a userId keyed object, and writes only after migration or signup token generation. Storage and JSON failures recover without throwing. The class exposes `DeviceConfig.Version` and `DeviceConfig.LocalStorageKey`, and accepts explicit version and storage parameters.

`npm run types -- --pretty false` and `git diff --check` passed. The client test harness could not reach its tests because the `better-sqlite3` native build failed; no test assertions ran. The work and verification notes are in `.codex-role-output/checkpoint.md`.