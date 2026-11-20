Implemented the chat message edit requirements across the API, messaging layer, route, client, socket fallback, and error language file. The edit API validates the message, checks edit permission, applies the change, and returns the updated message. The messaging layer now checks whether the message ID exists before editing.

`git diff --check` passes. The existing messaging tests could not start because Redis at `127.0.0.1:6379` is unavailable. Targeted ESLint reported unused parameters and imports in the touched files, along with long route lines.

The feature request’s `DirectedGraph` description does not match its concrete chat editing requirements; I implemented the listed requirements. Pre-existing untracked `appendonly.aof` remains untouched.