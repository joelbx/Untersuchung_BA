# Checkpoint

Resolved assistant upsell addon selection by using `getScribeAddonNameByPlan` from the payments/core public entrypoint. Removed the duplicate resolver and its Mail Plus fallback. Both paid flows now construct a `PlanIDs` object and add the Scribe addon only when the resolver returns one. Exported `SelectedPlan` and the resolver through payments/core and updated internal-path imports in call sites.

Verification:
- `yarn workspace @proton/components test --runInBand --watch=false hooks/assistant/assistantUpsellConfig.test.ts payments/core/subscription/selected-plan.test.ts`: passed (2 suites, 50 tests).
- `node_modules/.bin/prettier --check packages/components/hooks/assistant/assistantUpsellConfig.ts packages/components/hooks/assistant/assistantUpsellConfig.test.ts packages/components/payments/core/index.ts packages/components/hooks/assistant/useAssistantUpsellConfig.tsx packages/components/containers/payments/planCustomizer/ProtonPlanCustomizer.tsx`: passed.
- `git diff --check`: passed.

`rg` was unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used instead.
