Implemented chat privacy controls with `disableIncomingMessages`, UID allow and deny lists, and server-side checks for chat starts, room invitations, private room lookup, and messages in one-to-one rooms. Blocks take precedence; admins and global moderators bypass the lists.

Added the batched, repeat-safe migration in [chat_allow_list.js](/app/src/upgrades/4.3.0/chat_allow_list.js) and account settings controls. The legacy name remains only in migration code and cleanup for the installed theme’s old checkbox.

**Verification:** 353 messaging and user tests passed. ESLint, syntax checks, language JSON and OpenAPI parsing, and `git diff --check` passed.