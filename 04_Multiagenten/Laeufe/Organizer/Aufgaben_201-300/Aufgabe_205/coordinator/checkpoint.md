Task: implement centralized API token lifecycle utilities in src/api/utils.js.
Status: implemented lifecycle methods in src/api/utils.js and bearer verification support in src/routes/authentication.js. Added a focused in-memory lifecycle test. No delegation used.
Verification: mocha test/api-utils-tokens-unit.js passes; ESLint passes for changed JavaScript files. Existing database-backed authentication tests require the credential-bearing test database configuration and were not run.
