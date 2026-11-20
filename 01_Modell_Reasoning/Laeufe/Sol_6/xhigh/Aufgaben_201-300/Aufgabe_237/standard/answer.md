Implemented the listed chat editing requirements: the v3 PUT route validates edits, checks message existence and permission, and returns the updated message. The client now uses PUT for edits; the socket path warns that it is deprecated. I also added the error translation, OpenAPI entry, and tests.

Verification passed: 79 messaging tests, 975 API tests, and JSON/OpenAPI validation. Full lint still reports pre-existing errors in placeholder handlers and unrelated lines.

The `DirectedGraph` description does not match this checkout: its application source contains no `LinkProvider` to refactor.