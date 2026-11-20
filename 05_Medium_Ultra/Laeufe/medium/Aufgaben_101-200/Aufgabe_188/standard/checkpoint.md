# Storage size unification checkpoint

- Centralized `BASE_SIZE`, `sizeUnits`, and `SizeUnits` in `packages/shared/lib/helpers/size.ts`; `humanSize.ts` imports and reexports the units for compatibility.
- Migrated member allocation, invitation, organization setup, CSV parsing, bonus storage, offer displays, and remaining production byte calculations to the shared units.
- Removed `BASE_SIZE` and `GIGA` definitions from `packages/shared/lib/constants.ts`. No production `GIGA` or inline GB multipliers remain in the searched TypeScript source.
- Existing CSV import Jest suite passed: 64 tests, 5 snapshots. Prettier check passed for all edited files. Shared and component TypeScript checks are running.
- Shared and component type checks both stopped on the same existing error in `packages/crypto/lib/worker/api.ts:579`: incompatible `openpgp` types from two installed packages. No type errors were reported in edited files.
