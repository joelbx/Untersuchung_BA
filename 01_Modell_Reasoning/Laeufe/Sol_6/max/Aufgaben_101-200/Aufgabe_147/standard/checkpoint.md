# DeviceConfig issue checkpoint

- Objective: make initialization preserve persisted configuration, migrate credentials safely, and write only for migrations or a missing signup token.
- Repository: `/app`; target: `src/misc/DeviceConfig.ts`; existing tests: `test/client/misc/DeviceConfigTest.ts`.
- Initial git working tree was clean. `rg` is unavailable, so use `find` and `grep` for local inspection.
- Implemented a single config object, explicit version/storage injection, safe migration to a credential record, conditional writes, and complete underscored-key serialization.
- Added tests for current-version no-write loads, versions 1 and 2 migration, token generation, credential database-key preservation, and unavailable storage.
- Source and test TypeScript checks pass. The final client suite passed with 3,092 assertions (`npm run testclient -- -c`).
