# Checkpoint

Issue: assistant upsell config must use the centralized Scribe addon resolver and a shared `planIDs` shape in both flows, with public payments/core imports/exports.

Initial findings: implementation is in `packages/components/hooks/assistant/assistantUpsellConfig.ts`; tests are in its sibling `.test.ts`. `SelectedPlan` currently imports from an internal subscription path in the hook/test, and `getScribeAddonNameByPlan` exists in payments core subscription helpers.

Next: inspect public barrel exports and existing assertions, then update implementation, imports, exports, and tests only as needed; run the existing relevant test suite.
