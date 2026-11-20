Implemented WebFinger discovery at `/.well-known/webfinger`. The handler validates the resource and hostname, checks `view:users` permission (evaluating anonymous callers as Guest), resolves the user slug, and returns the subject, UID and slug aliases, and an HTML profile link.

ESLint passes. The controller tests could not run because the required Redis service is unavailable at `127.0.0.1:6379`.