Task: Fix Security Center PassAliases drawer and PassBridge vault contract.
Changes: Added provider hook and fetch/filter helpers; changed default-vault lookup to read only with explicit creation; added No aliases message and Get an alias action; updated focused UI test.
Verification: Components and Pass TypeScript checks passed. PassAliases.test.tsx passed (3 tests). git diff --check passed.
