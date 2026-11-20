Updated the expiry utility so cancellation context and disabled auto-renew use the current subscription term. The cancellation screens now display that term’s end date, while free-plan and ordinary renewal behavior remain unchanged.

Verification passed: 37 focused tests, the components typecheck, targeted ESLint and Prettier checks, and `git diff --check`.