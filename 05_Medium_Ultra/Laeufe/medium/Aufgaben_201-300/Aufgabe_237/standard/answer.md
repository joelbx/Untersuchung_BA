Implemented the chat editing requirements in `/app`: the v3 PUT route validates content and edit permission, returns the updated message, and uses the new `Messaging.messageExists` check. The client now sends edits by PUT, and the socket edit path logs a deprecation warning and validates its input.

The issue description also requests a `DirectedGraph` refactor, but this checkout has no `LinkProvider` implementation to refactor.

Verification: the messaging suite passed (76 tests), targeted ESLint passed, and `git diff --check` passed.