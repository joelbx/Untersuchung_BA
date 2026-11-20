Task: Add bounded event polling after payment method initiation.
Status: Implemented and verified.
Changes: usePollEvents exports interval=5000 and maxPollingSteps=5, supports optional property/action matching, stops on match or after five calls, and clears timer/subscription exactly once. New Chargebee card and PayPal payment methods watch PaymentMethods CREATE events. Added focused polling tests.
Verification: Component polling and EditCardModal tests passed (6 tests); @proton/components type check passed; git diff --check passed.
Constraints observed: No git history, index baseline, or harness configuration changes.
