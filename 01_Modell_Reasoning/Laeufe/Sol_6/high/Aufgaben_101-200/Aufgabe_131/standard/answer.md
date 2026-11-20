Added bounded event polling to the card and PayPal creation flows. The hook calls the event manager every 5 seconds, up to 5 times, and can stop early when a `PaymentMethods` creation event arrives. It unsubscribes on completion and ignores late events.

Verification passed: 6 polling tests, 10 existing payment tests, type checking, ESLint, and Prettier.