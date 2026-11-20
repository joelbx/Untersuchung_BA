Implemented chat allow and deny lists, an incoming chat disable setting, and server checks for direct messages, room creation, and invitations. Added an idempotent [upgrade](/app/src/upgrades/4.3.0/chat_allow_list.js) that seeds allow lists from legacy follows, plus account controls.

Verification passed: 81 messaging tests, 276 user tests, ESLint, and `git diff --check`.