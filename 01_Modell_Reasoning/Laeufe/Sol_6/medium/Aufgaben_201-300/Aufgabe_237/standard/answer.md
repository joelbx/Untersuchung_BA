Implemented the detailed chat-edit requirements: the v3 `PUT` route now validates and edits messages, returns the updated message, and rejects invalid content or IDs. The client uses that route, and the socket edit path logs a deprecation warning. Added integration tests for the new behavior.

The full messaging test file passes (**78 tests**). `git diff --check` and lint on the messaging, client, and test changes pass; full touched-file lint still reports preexisting errors.

The issue description calls for a `DirectedGraph`, but its detailed requirements specify chat editing. This change follows the detailed requirements.