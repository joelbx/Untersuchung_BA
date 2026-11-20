Added bounded event polling after the PayPal payment method flow. The hook now exports `interval = 5000` and `maxPollingSteps = 5`, can stop early on a matching `PaymentMethods` create event, and unsubscribes when polling finishes.

All five focused tests pass. The components type check, Prettier check, and `git diff --check` also pass.