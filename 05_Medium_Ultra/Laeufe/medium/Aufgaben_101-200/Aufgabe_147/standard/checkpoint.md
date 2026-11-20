Task: fix DeviceConfig non-destructive load/migration persistence.
Status: complete. DeviceConfig persists one config object with exact underscored keys, migrates legacy credential arrays to userId-keyed objects, preserves known fields, generates missing signup tokens, and skips load writes for current valid data. Focused tests added.
Verification: npm run testclient passed (3063 assertions); npm run types -- --pretty false passed; git diff --check passed.
Constraints followed: local code/tests only; no git history, index, or harness changes.
