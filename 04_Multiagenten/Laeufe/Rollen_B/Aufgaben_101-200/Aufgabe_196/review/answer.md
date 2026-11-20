VERDICT: FIX

**Code defect:** The free user upsell still hardcodes the Scribe addon in [assistantUpsellConfig.ts](/app/packages/components/hooks/assistant/assistantUpsellConfig.ts:18). Resolve the addon with `getScribeAddonNameByPlan(PLANS.MAIL)` and add it only when the resolver returns a name, as required for all flows.

**Tests:** `yarn workspace @proton/components test --runInBand --runTestsByPath hooks/assistant/assistantUpsellConfig.test.ts payments/core/subscription/selected-plan.test.ts` passed: 2 suites, 50 tests.

**TEST_ENVIRONMENT_PROBLEM:** None. This was an independent review; no project code was changed.