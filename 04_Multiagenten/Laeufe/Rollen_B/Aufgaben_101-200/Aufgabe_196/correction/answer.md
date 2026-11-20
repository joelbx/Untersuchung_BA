Fixed the free user upsell: it now resolves the Mail Scribe addon through `getScribeAddonNameByPlan` and adds it to `planIDs` only when the resolver returns a name.

The exact two test files flagged in review passed: **2 suites, 50 tests**. `git diff --check` also passed. No remaining failures or test environment problems.