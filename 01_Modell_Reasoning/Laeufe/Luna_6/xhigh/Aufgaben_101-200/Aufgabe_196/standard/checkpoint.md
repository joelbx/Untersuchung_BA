# Checkpoint

Task: Resolve assistant upsell addon inconsistency in `/app`.

Findings:
- The existing centralized `getScribeAddonNameByPlan` resolver lives in `payments/core/subscription/helpers.ts`.
- `payments/core/index.ts` did not export that resolver or `SelectedPlan`.
- The assistant upsell config contained a duplicate hardcoded resolver, and `SelectedPlan` consumers imported its internal file path.

Changes made:
- Exported the resolver and `SelectedPlan` from the payments/core public entry point.
- Reworked single and multi user config builders to construct `planIDs` objects and only add an addon when a resolver returns a name.
- Removed the duplicate resolver and switched all `SelectedPlan` consumers to the public entry point.

Verification:
- `git diff --check` passed.
- `yarn workspace @proton/components test hooks/assistant/assistantUpsellConfig.test.ts --runInBand` passed (1 suite, 9 tests).
- `yarn workspace @proton/components check-types --pretty false` reported one existing unrelated type error in `packages/crypto/lib/worker/api.ts:577` involving incompatible `openpgp` types; it reported no errors in the changed files.
