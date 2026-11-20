VERDICT: FIX
Review complete. Code defect: packages/components/hooks/assistant/assistantUpsellConfig.ts:18 still hardcodes MEMBER_SCRIBE_MAILPLUS in the free-user upsell. The issue requires a single resolver across all flows; use getScribeAddonNameByPlan(PLANS.MAIL) and add the addon only if returned.
Tests: `yarn workspace @proton/components test --runInBand --runTestsByPath hooks/assistant/assistantUpsellConfig.test.ts payments/core/subscription/selected-plan.test.ts` passed (2 suites, 50 tests).
TEST_ENVIRONMENT_PROBLEM: None.
No project code or tests changed during this independent review.
