Implemented event polling for new payment methods. The polling hook calls the event manager every 5000 ms for at most 5 attempts, stops early on a matching `PaymentMethods` create event, and unsubscribes on completion. Card and PayPal creation flows now use it.

Verification passed: 4 focused polling tests, the existing card and PayPal tests, TypeScript, Prettier, and `git diff --check`.