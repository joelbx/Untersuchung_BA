VERDICT: FIX

- [Container.tsx](/app/packages/components/containers/notifications/Container.tsx:28) can assign the same React key to two visible notifications: a success with ID `1` and an error with text `"1"`. Use distinct rendering keys while retaining the resolved `key` for deduplication.
- [Notification.tsx](/app/packages/components/containers/notifications/Notification.tsx:40) sets link attributes when the parent ref runs. A React child that adds a link later through its own state update can leave that link without `rel` or `target`. Apply the attributes when descendant links are added.

Tests executed: `yarn workspace @proton/components test notifications.test.tsx --coverage=false` passed (2 tests); `yarn workspace @proton/components check-types` passed. **TEST_ENVIRONMENT_PROBLEM:** none. No project code or tests were changed during this review.