Implemented bounded event polling for newly added card and PayPal methods. The hook calls the event manager every 5000 ms for up to 5 attempts, stops on a matching `PaymentMethods` create event, and unsubscribes when polling finishes.

Verification passed: 6 relevant tests, the components TypeScript check, and formatting checks.