# Checkpoint

Resolved assistant upsell addon selection through `getScribeAddonNameByPlan`, exported it and `SelectedPlan` from payments/core, and updated assistant imports. Both paid flows now build `planIDs` and add a Scribe addon only when the resolver supplies one. Added tests for unsupported plans in single-user and organization flows.

Verification:
- `yarn workspace @proton/components jest hooks/assistant/assistantUpsellConfig.test.ts payments/core/subscription/selected-plan.test.ts --runInBand --no-coverage`: passed, 2 suites and 50 tests.
- `yarn prettier --check packages/components/hooks/assistant/assistantUpsellConfig.ts packages/components/hooks/assistant/assistantUpsellConfig.test.ts packages/components/hooks/assistant/useAssistantUpsellConfig.tsx packages/components/payments/core/index.ts`: passed.
- `../../node_modules/.bin/eslint hooks/assistant/assistantUpsellConfig.ts hooks/assistant/assistantUpsellConfig.test.ts hooks/assistant/useAssistantUpsellConfig.tsx payments/core/index.ts --quiet` from `packages/components`: passed.
- `git diff --check`: passed.
- `yarn workspace @proton/components check-types`: failed (exit 2) at `../crypto/lib/worker/api.ts(577,77)` with TS2345. The installed `openpgp` and `pmcrypto/node_modules/openpgp` types disagree on `PartialConfig.preferredHashAlgorithm` (`hash.md5` incompatibility). This is outside the edited files; the full component type check remains unverified due to this error.
- An attempted `yarn eslint ... --quiet` from the repository root could not run because the root workspace has no `eslint` script; the direct local eslint binary command above completed successfully.
