Implemented user scoped property storage.

- Added `model.UserPropsRepository`, `DataStore.UserProps`, and the SQL implementation, which scopes CRUD operations to the user in context.
- Added a migration creating `user_props` and transferring existing Last.fm session keys for known users.
- Updated Last.fm session key handling to use `sessionKeyProperty` and the contextual repository; added request ID and user details to related error logs.
- Added persistence tests for CRUD, user isolation, and missing user context.

Verification passed: `go test ./...`, focused persistence and Last.fm tests, and `git diff --check`.