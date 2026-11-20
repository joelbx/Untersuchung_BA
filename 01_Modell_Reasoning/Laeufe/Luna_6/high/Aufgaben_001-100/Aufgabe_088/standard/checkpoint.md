# Checkpoint

Issue: support field selection in `getObject`/`getObjects` on MongoDB, Postgres, and Redis, with `[]` meaning the complete stored object.

Implemented:
- Added optional `fields = []` parameters to the public single and multi-object getters.
- Kept empty-field helper calls equivalent to full-object reads across all three backends.
- Preserved requested field names with `null` values when a stored object lacks a requested field.
- Preserved input key order and returned falsy values for missing records from the public getters.
- Added database hash regression cases for selection, empty fields, missing keys, and ordering.

Validation: ESLint, `node --check`, and `git diff --check` pass. The existing `test/database.js --grep 'Hash methods'` suite could not initialize because Redis at `127.0.0.1:6379` refused the connection.
