VERDICT: ACCEPT
Reviewed src/controllers/well-known.js, src/routes/well-known.js, and route/controller composition.
Evidence: resource validation rejects missing/malformed/wrong-host acct URIs; privileges.global.can("view:users", req.uid || 0) checks Guest for anonymous; slug lookup returns 404 when absent; JRD includes subject, UID/slug aliases, HTML profile link.
Tests: ./node_modules/.bin/mocha test/well-known.js — 4 passing (exit 0).
Lint: ./node_modules/.bin/eslint src/controllers/well-known.js src/routes/well-known.js test/well-known.js — exit 0.
Code defects: none found. TEST_ENVIRONMENT_PROBLEM: none.
