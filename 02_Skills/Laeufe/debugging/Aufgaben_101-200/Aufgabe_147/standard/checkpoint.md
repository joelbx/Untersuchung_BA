# DeviceConfig checkpoint

Status: investigating root cause before edits. `rg` is unavailable (`rg --files ...` exited 127: command not found); using local `find`/`grep` for discovery. No repository changes made yet.

Root cause confirmed: `_load()` writes a partially populated instance before assigning several fields, and V2 migration leaves `_credentials` as an array without updating `_version`. Regression: `npm run testclient` exited 1 with `DeviceConfig > migrateConfig > migrating from v2 to v3 preserves internal logins`: array should deep equal keyed object (1 of 3050 assertions failed).

Implemented: single typed config object; exact underscored persisted keys; keyed credential migration and Map reconstruction; initialization writes only after migration or missing-token generation; guarded unchanged setter writes; explicit static version/storage key and global constructor arguments. Added tests for no-write load, field-preserving migration, idempotence, and invalid/inaccessible storage.

Verification: `npx tsc --noEmit --pretty false` exited 0. `npm run testclient` exited 0 with all 3062 assertions passed (old style total: 3554). `git diff --check` exited 0. A clean client run (`cd test && node --icu-data-dir=../node_modules/full-icu test client -c`) built the new cases but exited 1 on an unrelated `OfflineDbTest` encryption assertion; the following full client run passed. The clean run also surfaced a test mock type error, which was corrected before the final successful run.
