# Checkpoint

Implemented actor-scoped posting locks in `src/controllers/write/topics.js`. Topic creation and replies acquire an atomic counter lock under the shared `locks` object, reject overlapping attempts with `[[error:already-posting]]`, and decrement the counter in `finally` after accepted work completes. User IDs identify authenticated actors; guest session IDs identify guest actors.

Validation: ESLint passes for the modified controller. The existing targeted topic test (`npm test -- --grep "post a topic as guest"`) could not initialize because Redis at `127.0.0.1:6379` refused the connection; no tests ran.
