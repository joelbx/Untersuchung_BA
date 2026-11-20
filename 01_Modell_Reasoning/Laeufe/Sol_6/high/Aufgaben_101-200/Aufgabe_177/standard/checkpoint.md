# Chat allow/deny list work

Status: complete.

Changed account settings to use disableIncomingMessages, chatAllowList, and chatDenyList. Added safe list parsing and serialization, server-side privacy checks for chat initiation and room creation/invites, account controls, English labels, and an idempotent 4.3.0 upgrade that seeds the allow list from follows. Restricted legacy users with no follows are migrated to disabled incoming messages so their prior restriction remains effective.

Verification: 356 tests passed in test/messaging.js and test/user.js. Targeted ESLint, JSON parsing, and git diff --check passed. A temporary local Redis instance was used for the tests.
