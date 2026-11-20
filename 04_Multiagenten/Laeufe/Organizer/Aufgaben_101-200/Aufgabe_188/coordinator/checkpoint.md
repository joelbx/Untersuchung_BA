# Checkpoint

Task: centralize storage size unit definitions in packages/shared/lib/helpers/size.ts and update consumers.
Status: implementation complete. Added BASE_SIZE and sizeUnits as the sole production definitions; migrated member allocation, organization setup, CSV import, bonus storage, calendar/contacts imports, offer/referral displays, and drive limits.
Verification: components CSV Jest suite passed (64 tests, 5 snapshots); focused components and shared ESLint passed; git diff --check passed. Components TypeScript check was attempted and failed in unrelated packages/crypto/lib/worker/api.ts due to incompatible openpgp and pmcrypto openpgp types.
Delegation: none.
