# Checkpoint

Task: centralize storage size constants through @proton/shared/lib/helpers/size.
Completed: added authoritative BASE_SIZE/sizeUnits and migrated member provisioning, CSV, organization, shared constants, offers, referral, Drive, preview, and logo upload calculations.
Validation: CSV Jest suite passed (64 tests, 5 snapshots); Prettier and git diff --check passed. Shared and components type checks each fail only at packages/crypto/lib/worker/api.ts:579 due conflicting OpenPGP dependency types.
