Updated [removeTechnicalFields](/app/src/api/common/utils/EntityUtils.ts) to remove prefixed fields attached to nested `Date` and typed-array objects while retaining cycle protection. Fixed the post-mutation test type and added coverage for those objects.

`npm run test:app` and `npm run fasttest` both passed with 8,683 assertions. No remaining failures or test environment problems.