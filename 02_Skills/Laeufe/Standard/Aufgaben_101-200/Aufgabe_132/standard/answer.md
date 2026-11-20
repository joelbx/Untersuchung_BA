Reserved tags can now be configured in `meta.config.systemTags`. Topic creation, editing, queued posts, and the add-tags API reject them for unprivileged users with **“You can not use this system tag.”** The `isTagAllowed` check also reports reserved tags as unavailable.

Verification passed: 168 topic tests, 6 category whitelist tests, ESLint, and `git diff --check`.