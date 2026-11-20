# Checkpoint

Task: resolve the PassAliases drawer rendering and creation flow issue in `/app`.

Completed:
- Added the typed `usePassAliasesSetup` hook and `fetchPassAliases`/filter helpers.
- Updated the provider to expose `PassAliasesProviderReturnedValues`.
- Split bridge vault lookup from explicit Personal vault creation; updated the bridge mock for the new contract.
- Added an explicit “No aliases” empty state and ensured alias creation can initialize a missing vault.

Verification:
- `yarn workspace @proton/components test --runInBand --silent components/drawer/views/SecurityCenter/PassAliases/PassAliases.test.tsx` passed (3 tests).
- `yarn workspace @proton/components check-types --pretty false` passed.
- `git diff --check` passed.
