# Checkpoint

Task: repair DeviceConfig load, migration, and persistence behavior.
Status: complete.
Changes: persisted fields live in one config object; credentials deserialize to a Map and serialize under `_credentials`; migration preserves known fields; initialization writes only for migration or missing signup token; writes deduplicate unchanged state; storage failures recover.
Verification: `npx tsc --noEmit --pretty false` passed; `npx tsc -p test/tsconfig.json --pretty false` passed; `npm run testclient` passed (3,077 assertions); `git diff --check` passed.
Constraints: local code/tests only; no git history/index/harness changes.
