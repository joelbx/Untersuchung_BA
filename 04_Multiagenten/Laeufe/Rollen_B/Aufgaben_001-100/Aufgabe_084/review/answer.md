VERDICT: FIX

- **Code defect:** [EntityUtils.ts](/app/src/api/common/utils/EntityUtils.ts:143) skips nested `Date` and typed-array objects, leaving any prefixed properties attached to them. Traverse their own properties while retaining the cycle guard.
- **Test defect:** [EntityUtilsTest.ts](/app/test/tests/api/common/utils/EntityUtilsTest.ts:73) compares the inferred entity type with an expected object missing fields that the type still requires. Widen the assertion type for this post-mutation comparison.

`npm run test:app` failed during TypeScript compilation with TS2739 and TS2322 at test lines 76–77. `npm run fasttest` passed: 8,679 assertions. **TEST_ENVIRONMENT_PROBLEM:** none identified. No project code or tests were edited during this review.