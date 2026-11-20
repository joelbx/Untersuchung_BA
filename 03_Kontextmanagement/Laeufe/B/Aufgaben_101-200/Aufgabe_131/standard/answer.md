Implemented bounded event polling for the card and PayPal add flows. The hook calls the event manager every 5 seconds, up to 5 times, and stops early when it receives a matching `PaymentMethods` create event. It unsubscribes on completion and ignores late events.

Validation passed: 5 Jest tests, the component TypeScript check, and formatting checks.