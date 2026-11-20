Implemented generic `P` and nil-safe `V`, and changed nullable external-info and share-expiration timestamps to pointers. Updated timestamp reads and assignments accordingly, with helper tests covering zero and nil values.

The existing tests passed: `go test ./utils/gg ./model ./core ./server/subsonic ./server/public ./scanner`. `git diff --check` also passed.