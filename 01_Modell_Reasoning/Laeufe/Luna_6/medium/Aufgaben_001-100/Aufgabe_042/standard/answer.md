Implemented `/.well-known/webfinger` with resource validation, `groups:view:users` authorization using UID `0` for anonymous requests, user lookup, and a WebFinger JSON response. Registered the controller and mounted the route in the main route composition.

ESLint and `git diff --check` passed. The focused existing controller tests could not run because Redis at `127.0.0.1:6379` was unavailable.