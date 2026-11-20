# Checkpoint

Task: resolve the assistant upsell addon resolver/config inconsistency in `/app`.

Findings: the payments/core subscription helpers already provide `getScribeAddonNameByPlan`; assistant upsell config duplicated its mapping and imported `SelectedPlan` internally. The public `payments/core` barrel did not export either symbol. The upsell test and plan customizer also imported `SelectedPlan` by internal path.

Changes made: exported the resolver and `SelectedPlan` from the public core barrel; removed the duplicated resolver; used the centralized resolver in free and paid upsell flows; constructed explicit `planIDs` objects for single and multiple user configs, with addon inclusion conditional; made `addonName` optional in both paid config functions; moved affected imports to the public entrypoint.

Validation:
- `yarn workspace @proton/components test hooks/assistant/assistantUpsellConfig.test.ts --runInBand` passed (9 tests).
- `git diff --check` passed.
- Search found no stale `paidUserAssistantAddonName` calls or public consumers importing through `payments/core/subscription/...`.
- `yarn workspace @proton/components check-types --pretty false` reported one error in `packages/crypto/lib/worker/api.ts:577`, involving incompatible OpenPGP `PartialConfig` types. No diagnostics pointed to the changed files.
