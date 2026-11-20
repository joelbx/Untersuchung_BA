Updated assistant upsell configuration to use `getScribeAddonNameByPlan` and build `planIDs` consistently in both paid flows. Exported `SelectedPlan` and the resolver from `payments/core`, and switched assistant call sites to that public entry point.

`git diff --check` passed. The focused Jest run produced no output during initialization, so I interrupted it; the test result is unverified.