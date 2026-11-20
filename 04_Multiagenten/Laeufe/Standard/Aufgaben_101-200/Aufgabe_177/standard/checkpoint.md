# Chat allow/deny list checkpoint

Implemented disableIncomingMessages, chatAllowList, and chatDenyList in user settings and account controls. Server checks blocks first, then privacy rules, with admin and global moderator exemptions. Added batched, idempotent migration from legacy restricted-chat follow lists and applied checks to API and federated chat initiation. Updated schema, language, and tests.

Verified: messaging (78 passing), user (276 passing), ActivityPub private objects (3 passing), ESLint, JSON parsing, and git diff --check. No known remaining work.
