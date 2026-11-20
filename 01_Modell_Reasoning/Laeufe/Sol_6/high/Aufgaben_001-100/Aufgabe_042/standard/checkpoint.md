Task: Implement WebFinger at /.well-known/webfinger in /app.
Status: Complete. Added dedicated controller and route, registered in core route composition, and added focused tests.
Behavior: Validates acct resource and configured hostname; checks global view:users permission with uid 0 for absent req.uid (Guest); resolves user slug; returns JRD JSON with subject, UID/profile aliases, and HTML profile link. Returns 400, 403, or 404 as required.
Verification: node_modules/.bin/mocha test/well-known.js --reporter spec (6 passing); ESLint on changed JavaScript files (passing); git diff --check (passing).
Constraints: Used local code and tests only; did not change git history, index, or harness configuration.
