Task: Add optional field selection to db.getObject and db.getObjects across MongoDB, Postgres, and Redis. Empty fields must fetch complete objects; requested missing fields become null; missing keys and input order retain existing contracts.

Progress: Updated MongoDB, Postgres, and Redis hash retrieval methods to accept optional fields. Empty or omitted fields fetch complete objects; selected fields include null for absent fields and return null for missing keys. Postgres projection SQL now handles empty field lists. Added and adjusted hash regression tests for selection, empty fields, missing keys, and order.

Verification: `node_modules/.bin/mocha test/database/hash.js` passed (57 tests) against local Redis; ESLint and `git diff --check` passed. MongoDB and Postgres services are unavailable in this workspace, so those backends were reviewed statically.
