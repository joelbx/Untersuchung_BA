Task: Add bounded event polling after initiating a payment method, with matching event early stop and cleanup.
Status: Implemented bounded event polling with matching event early completion and subscription cleanup. Connected card and PayPal creation flows; added focused tests.
Verification: Six focused polling tests passed; ten existing payment tests passed; components type checking, targeted ESLint, Prettier, and git diff checks passed.
Constraints: Local code and tests only; preserve git history/index and harness configuration.
