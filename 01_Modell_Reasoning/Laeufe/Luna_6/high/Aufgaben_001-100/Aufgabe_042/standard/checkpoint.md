# Checkpoint

Task: implement `GET /.well-known/webfinger` with resource validation, authorization through the existing privileges API (including Guest for anonymous callers), user lookup, and WebFinger JSON; mount it in the application routes and run existing relevant tests.

Implemented the controller in `src/controllers/well-known.js`, registered it in `src/controllers/index.js`, added `src/routes/well-known.js`, and mounted that route in `src/routes/index.js`. The handler uses `privileges.global.can('view:users', req.uid || 0)` so anonymous callers are evaluated as Guests.

Verification: ESLint passes for all changed JavaScript files. `npx mocha test/controllers.js` was attempted, but its root setup hook failed before tests ran because Redis is unavailable (`ECONNREFUSED 127.0.0.1:6379`).
