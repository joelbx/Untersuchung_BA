Task: Fix cancellation expiry display when a future plan change is scheduled.
Status: Complete. Updated expiry utility and cancellation date displays; added regression tests for the active term and preserved normal renewal behavior.
Verification: 42 focused Jest tests passed across four suites; components TypeScript check passed; Prettier and git diff checks passed.
Constraints: Use local code and existing tests only. Preserve free-plan and non-cancellation behavior.
