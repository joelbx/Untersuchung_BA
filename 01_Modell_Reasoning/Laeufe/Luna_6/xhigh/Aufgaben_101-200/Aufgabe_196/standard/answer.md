Implemented the assistant upsell changes. Both paid flows now build a `planIDs` object and add an addon only when the centralized resolver returns one. Exported `SelectedPlan` and `getScribeAddonNameByPlan` from the payments/core entry point and updated imports to use it.

The assistant upsell tests passed: **9 tests**. Type checking reported one error in `packages/crypto/lib/worker/api.ts:577`, involving incompatible `openpgp` types; it reported no errors in the changed files.

Changed: [assistantUpsellConfig.ts](/app/packages/components/hooks/assistant/assistantUpsellConfig.ts), [core/index.ts](/app/packages/components/payments/core/index.ts), and the affected `SelectedPlan` consumers.