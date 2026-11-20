# Work checkpoint

Task: implement the concrete chat editing requirements in /app. The issue description mentions LinkProvider and DirectedGraph, but no LinkProvider or graph code exists in the checked-out application source.

Completed: enabled PUT /chats/:roomId/:mid with room assertion; validated content, message existence, room ownership and edit permission; returned updated v3 response; added Messaging.messageExists and edit guard; moved client editing to PUT; preserved POST sending and hook payload; added socket deprecation and input validation; added en-GB error string and OpenAPI route; expanded messaging and API tests.

Verification: test/messaging.js: 79 passing; test/api.js: 975 passing; OpenAPI parser validation passed; changed JavaScript passed syntax checks. Full lint has pre-existing errors in placeholder chat handlers, long existing route lines and unused socket imports; changed functional code passes with those existing rules suppressed. Source JSON remains authoritative for translations; local tests use stale generated language assets.

Repository state: working-tree edits only. Existing untracked appendonly.aof left untouched. No git index or history changes.
