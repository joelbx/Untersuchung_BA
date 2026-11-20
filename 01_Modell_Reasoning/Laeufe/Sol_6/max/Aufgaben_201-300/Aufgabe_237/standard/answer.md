Implemented the chat requirements in `/app`: the [v3 edit endpoint](/app/src/controllers/write/chats.js:69) validates content and permissions, [Messaging.messageExists](/app/src/messaging/index.js:15) guards edits, the [client](/app/public/src/client/chats/messages.js:10) uses POST and PUT, and the legacy socket path warns and validates input. I also added the error text and OpenAPI documentation.

The messaging suite passed **77 tests** and the API suite passed **975 tests**. ESLint still reports pre-existing warnings in touched files.

The `DirectedGraph` description does not match this checkout: it contains no `LinkProvider` or link analysis code to refactor.