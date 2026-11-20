Implemented the chat messaging requirements in `/app`: REST message edits now validate content, check edit permission, return updated message data, and use `PUT` from the client. I also added `Messaging.messageExists`, missing-ID handling, the error text, and socket edit deprecation and input validation.

The full messaging suite passes: **76 tests**. `git diff --check` passes. ESLint passes for the changed client, messaging, and test files; the controller, route, and socket files still report preexisting lint errors.

I found no `LinkProvider` or graph implementation in this checkout, so the requested `DirectedGraph` refactor could not be applied here.