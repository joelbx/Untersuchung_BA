# Fault localization checkpoint

Scope: inspected local source and existing tests only. No project source or tests changed. `rg` unavailable; used targeted reads and grep.

Findings:
- `src/controllers/write/chats.js`: `Chats.messages.edit` is a stub. `src/routes/write/chats.js`: PUT `/:roomId/:mid` route is commented out.
- `src/messaging/index.js`: no `messageExists`; existing `roomExists` uses `db.exists`, and messages use `message:${mid}` keys. `src/messaging/edit.js`: `editMessage` checks content but not existence; `canEdit` checks ownership/system and policy using message fields.
- `public/src/client/chats/messages.js`: new sends already use `api.post` with `{ message: msg }`, and `action:chat.sent` already carries `message` and `mid`; local variable is `msg`. Edits still use socket emit.
- `src/socket.io/modules.js`: `chats.edit` lacks deprecation warning and does not require `mid`; other socket methods show `sockets.warnDeprecated` convention.
- `public/language/en-GB/error.json`: `invalid-mid` absent.
- `test/messaging.js`: existing socket edit tests cover malformed data, blank message, non-owner, successful edit; no v3 edit or messageExists coverage found.
- Issue title/description request DirectedGraph, but concrete requirements are chat-specific; no `DirectedGraph` or `LinkProvider` symbols found in local app source/tests.

Likely fix behavior: validate missing/blank content as 400 invalid-chat-message; check message existence before edit as invalid-mid; deny unauthorized/system edits as 400 cant-edit-chat-message; persist edit and return formatted v3 updated message; route with room assertion; client PUT edit; deprecate socket edit and reject malformed input. Open question: room assertion checks membership in requested room but does not ensure `mid` belongs to it.
