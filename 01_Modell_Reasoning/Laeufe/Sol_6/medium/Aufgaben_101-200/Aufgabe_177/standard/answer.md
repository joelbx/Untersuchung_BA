Implemented chat privacy settings with an incoming chat disable switch and allow and deny lists. Server checks now give explicit user blocks priority, apply the lists to chat initiation and room invitations, and exempt admins and global moderators from the privacy settings.

Added a repeatable [upgrade](/app/src/upgrades/4.3.0/chat_allow_list.js) that seeds allow lists from follows for accounts with the old restriction enabled. Updated account controls, API schema, labels, and tests.

Verification: 77 messaging tests and 276 user tests passed; ESLint and `git diff --check` passed.