Added bounded event polling for new Chargebee card and PayPal payment methods. The hook calls the event manager at 5000 ms intervals, up to five times, and can stop early when a matching property and action event arrives. It clears its timer and subscription on completion and ignores late events.

Hook tests, payment flow tests, TypeScript, formatting, and `git diff --check` passed.