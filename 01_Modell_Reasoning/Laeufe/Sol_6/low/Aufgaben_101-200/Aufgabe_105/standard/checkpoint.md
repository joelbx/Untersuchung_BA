Task: Make getOpenSubsonicExtensions public while preserving JSON format and three extensions.
Status: Complete. Registered the endpoint before a protected route group; required parameter checks, authentication, and access updates now apply to the protected group. Added a request test for both route forms, unauthenticated JSON, and the exact three extensions.
Verification: go test ./server/subsonic ./server/subsonic/responses passed.
