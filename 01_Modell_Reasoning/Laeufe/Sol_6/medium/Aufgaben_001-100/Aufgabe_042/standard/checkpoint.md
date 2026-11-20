Task: Add WebFinger endpoint at /.well-known/webfinger.
Status: Complete. Added dedicated controller and router, wired into core route composition.
Behavior: Validates acct resource and configured hostname; checks view:users via global privileges (UID 0 for Guest); resolves userslug to UID; returns JRD subject, UID and profile aliases, and HTML profile link. Returns 400, 403, or 404 as appropriate.
Verification: ESLint and Node syntax checks passed; isolated controller checks covered validation, Guest denial, missing user, and success. Existing database-backed tests were not run because their setup reads and logs local configuration, which may contain credentials.
