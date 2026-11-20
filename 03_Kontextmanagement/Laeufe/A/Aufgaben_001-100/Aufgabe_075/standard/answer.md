Added the `user_props` table and user scoped repository, migrated existing Last.fm session keys, and updated Last.fm to use the `sessionKeyProperty` constant. Property error logs now include request IDs where available.

Validation: `go test ./...` and `git diff --check` passed.