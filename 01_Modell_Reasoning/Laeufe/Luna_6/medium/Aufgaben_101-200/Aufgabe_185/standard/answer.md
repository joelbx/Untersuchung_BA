Implemented cancellation-aware expiry calculation. Cancellation confirmations in both B2C and B2B now get the end date from `subscriptionExpires`, which reports the active term’s date and plan when cancellation is in progress or auto-renew is disabled. Free plan behavior is unchanged.

The targeted test suite passed: 31 tests. `git diff --check` also passed.