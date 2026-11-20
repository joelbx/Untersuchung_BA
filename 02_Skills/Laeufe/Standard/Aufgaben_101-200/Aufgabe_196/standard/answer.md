Resolved the assistant upsell inconsistency. Both paid flows now build `planIDs` and add a Scribe addon only when the shared resolver returns one. The duplicate mapping is removed, and call sites import `SelectedPlan` and `getScribeAddonNameByPlan` from the payments/core public entrypoint.

Verification passed: 50 tests across two suites, Prettier, and `git diff --check`.