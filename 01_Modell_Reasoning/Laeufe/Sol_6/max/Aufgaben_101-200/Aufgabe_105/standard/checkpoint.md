Task: Make getOpenSubsonicExtensions public while preserving JSON format and its three extensions.
Status: Complete. Registered the extensions route outside the protected group; kept required-parameter, authentication, and last-access middleware on all other routes. Added router coverage for credential-free JSON responses on both URL forms and continued authentication on /ping.
Verification: go test ./server/subsonic/... passed; git diff --check passed.
