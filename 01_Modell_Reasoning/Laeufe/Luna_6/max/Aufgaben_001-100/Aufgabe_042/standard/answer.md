Implemented `GET /.well-known/webfinger` with resource and hostname validation, Guest-aware `groups:view:users` authorization, user lookup, and a WebFinger JSON response with UID and slug profile aliases.

Added the handler in [well-known.js](/app/src/controllers/well-known.js), the route in [well-known.js](/app/src/routes/well-known.js), and integrated both into the controller exports and route composition.

ESLint and `git diff --check` passed. The controller suite reported 140 passing and 1 unrelated failure: the user data export test received an empty response body.