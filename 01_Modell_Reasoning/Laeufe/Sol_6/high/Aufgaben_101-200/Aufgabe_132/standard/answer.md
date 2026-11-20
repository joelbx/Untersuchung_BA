Reserved tags are now configurable through `meta.config.systemTags`. Topic creation, editing, queued posts, and the REST tagging endpoint reject them for unprivileged users with **“You can not use this system tag.”** The `isTagAllowed` check also reports reserved tags as unavailable.

Verification passed: 169 topic tests, 153 post and category tests, ESLint, and `git diff --check`.