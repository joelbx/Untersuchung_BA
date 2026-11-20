# Chat privacy issue checkpoint

Implemented disableIncomingMessages, chatAllowList, and chatDenyList with safe storage/loading, account management controls, and documentation. Permission checks now report explicit blocks first, apply disable/deny/allow rules, and exempt administrators and global moderators from list restrictions. Direct room creation and user addition check recipient privacy in the messaging library. Added repeatable 4.3.0 migration from legacy restrictChat follow lists; accounts with no follows remain closed to incoming chats.

Verification: `npx mocha test/messaging.js test/user.js` passed (353 tests). After final room and test edits, `npx mocha test/messaging.js --reporter dot` passed (78 tests). ESLint on changed JavaScript and `git diff --check` passed. No delegation used.
