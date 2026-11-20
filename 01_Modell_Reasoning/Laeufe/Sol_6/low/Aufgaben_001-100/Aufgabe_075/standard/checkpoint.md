Task: implement user-scoped user_props storage, datastore API, Last.fm migration, and run relevant existing tests.
Status: complete. Added migration with legacy Last.fm key transfer, contextual SQL repository and datastore method, updated Last.fm agent/router and mock datastore, added isolation test. `go test ./...` passed.
