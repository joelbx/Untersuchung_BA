Implemented the chat edit requirements in the checked-out repository: the PUT route validates content, checks edit permission and message existence, applies the edit, and returns the updated message in a v3 response. Client edits now use PUT; the old socket path warns that it is deprecated and validates its input.

The supplied `DirectedGraph` description does not match this checkout: I found no `LinkProvider` or link analysis code to refactor.

Verification: the messaging suite passed (**77 tests**), focused ESLint passed, and `git diff --check` passed. No delegation was used.