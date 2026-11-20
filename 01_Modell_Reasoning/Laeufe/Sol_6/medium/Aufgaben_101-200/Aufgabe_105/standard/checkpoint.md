# Checkpoint

Task: make getOpenSubsonicExtensions public while preserving JSON formatting and the three advertised extensions.
Status: complete.
Changes: public route is registered after form parsing and before a protected route group; existing extension handler remains unchanged. Added route tests for both URL forms, JSON content, and a protected endpoint's required-parameter behavior.
Verification: GOPROXY=off GOSUMDB=off go test ./server/subsonic passed; git diff --check passed.
