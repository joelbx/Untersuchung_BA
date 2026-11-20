Task: implement chat:privileged global permission across chat middleware, messaging, invitations, profile API, admin i18n, and OpenAPI.
Status: complete. Registered the privilege and label; global.can now accepts strings or arrays; chat paths use array privilege checks; canMessageUser requires chat:privileged for privileged targets; profile canChat reflects canMessageUser; OpenAPI updated.
Verification: mocha test/messaging.js test/middleware.js: 91 passing. ESLint on changed JS files: passing. git diff --check: passing.
