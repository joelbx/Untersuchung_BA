Implemented the assistant upsell changes. Both paid config builders now support an optional addon and build `planIDs` consistently. Addon names come from `getScribeAddonNameByPlan`, and `SelectedPlan` plus the resolver are exported through `@proton/components/payments/core`.

The existing assistant upsell test suite passed: **9/9 tests**. `git diff --check` passed.