I located the enforcement gaps, but **did not edit project source or tests**: the specialist instructions for this run require a diagnosis only.

- [src/topics/tags.js](/app/src/topics/tags.js:63): `validateTags(tags, cid)` checks tag counts but has no user ID or reserved tag check. `createTags` writes tags without checking authorization.
- [src/topics/create.js](/app/src/topics/create.js:72), [src/posts/edit.js](/app/src/posts/edit.js:134), and [src/posts/queue.js](/app/src/posts/queue.js:219): validation calls need the acting user’s ID. The queue call also omits the category ID.
- [src/controllers/write/topics.js](/app/src/controllers/write/topics.js:88): the tag adding API calls `createTags` directly, bypassing validation.
- [src/socket.io/topics/tags.js](/app/src/socket.io/topics/tags.js:9): `isTagAllowed` checks only the category whitelist.
- [install/data/defaults.json](/app/install/data/defaults.json:28): `systemTags` has no default. [src/user/index.js](/app/src/user/index.js:157) provides `isPrivileged(uid)`; it includes administrators, global moderators, and moderators of any category.

A fix should reject reserved tags for unprivileged users with the exact message `You can not use this system tag.` across creation, editing, queued posts, and the tag adding API, and make `isTagAllowed` exclude reserved tags. The remaining ambiguity is whether “privileged” means the existing global `isPrivileged` definition or privilege in the topic’s specific category. I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).