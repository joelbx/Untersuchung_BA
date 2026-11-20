The payment polling hook now calls the event manager every 5000 ms for up to five attempts. It can stop early when a specified property and action appear, and it unsubscribes when polling completes. The add PayPal flow now watches for a `PaymentMethods` create event.

The focused tests (4), components TypeScript check, formatting check, and diff check all passed.