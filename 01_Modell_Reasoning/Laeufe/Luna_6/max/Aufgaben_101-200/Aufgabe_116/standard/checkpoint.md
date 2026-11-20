# Checkpoint

Task: implement the privileged-chat gate in `/app`.

Initial status: working tree was clean. `rg` is unavailable in this environment, so repository discovery used `find` and standard text utilities.

Implemented so far: registered the global `chat:privileged` privilege; made `privileges.global.can` return a boolean for one privilege and boolean arrays for privilege arrays; enforced basic versus privileged target permissions in messaging; updated chat middleware, room/message flows, and invites; and added `canChat` to profile responses, OpenAPI, and English admin translations.

Validation: targeted ESLint passed; OpenAPI YAML and both English locale JSON files parse; `git diff --check` passed. The existing `npm test -- --grep 'Messaging Library'` command could not start its tests because Redis at `127.0.0.1:6379` was unavailable (failure occurred in the test setup hook before tests ran).

Final review: changes are limited to the privilege implementation, messaging/chat checks, profile responses, OpenAPI, and English admin translations. No test or harness files were changed.
