Task: Correct cancellation expiry dates for subscriptions with a scheduled plan change.
Status: Complete. subscriptionExpires uses the active term during cancellation or when current auto-renew is disabled. Cancellation date displays use the utility. Focused tests passed (40 initial tests plus 7 in the updated confirmation suite), package type check passed, and git diff --check passed.
Constraints: Use repository code and existing tests only; preserve git history, index baseline, and harness configuration.
