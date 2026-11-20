# Checkpoint

Task: Centralize storage unit usage on `@proton/shared/lib/helpers/size`.

Completed: Added `BASE_SIZE` and `sizeUnits` in `helpers/size.ts`. Updated shared constants, formatting, limits, member provisioning, CSV import, organization setup, and storage displays to use the centralized units. Removed the old `GIGA` and `BASE_SIZE` definitions from `constants.ts`. Added a regression test for the one-tebibyte Drive allocation.

Verification: CSV import Jest suite (64 tests), humanSize Jest suite (15 tests), and MemberStorageSelector default storage Jest suite (4 tests) passed. ESLint on changed files and `git diff --check` passed. Shared and components TypeScript checks both report the same existing `openpgp` type incompatibility in `packages/crypto/lib/worker/api.ts:579`; no edited file was reported. The shared Karma runner could not launch its configured Playwright Chrome binary; the humanSize suite passed through Jest instead.
