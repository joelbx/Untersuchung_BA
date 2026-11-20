Fixed the cancellation expiry date. The expiry utility now uses the active subscription term when cancellation is in progress or auto-renew is disabled, and the cancellation screens display that date instead of a scheduled future term’s date. Normal renewal and free-plan behavior remain unchanged.

Verification passed: 53 relevant tests, the components type check, and `git diff --check`.