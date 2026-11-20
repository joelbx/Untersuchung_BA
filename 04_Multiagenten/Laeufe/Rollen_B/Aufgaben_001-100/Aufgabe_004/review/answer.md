VERDICT: FIX

**Code defect:** [PassBridgeFactory.ts](/app/packages/pass/lib/bridge/PassBridgeFactory.ts:60) returns a newly created vault for every later `getDefault` call with a positive `maxAge`, without checking its age or active state. If that vault is removed or trashed, the drawer can keep selecting it indefinitely. Make the created vault obey the requested TTL or refresh the default-vault lookup after creation.

**Tests executed:** The existing PassAliases test command passed (2 suites, 6 tests): `yarn workspace @proton/components test --runInBand --watch=false components/drawer/views/SecurityCenter/PassAliases/PassAliases.test.tsx components/drawer/views/SecurityCenter/PassAliases/PassAliasesError.test.ts`. Both `yarn workspace @proton/components check-types --pretty false` and `yarn workspace @proton/pass check-types --pretty false` passed. The tests mock the provider context, so they do not cover this bridge behavior.

**TEST_ENVIRONMENT_PROBLEM:** None. Project code was left unchanged for this independent review.