Reserved tags can now be configured through `meta.config.systemTags`. Topic creation, editing, queueing, and the tag write API reject their use by unprivileged users with the message “You can not use this system tag.” The socket `isTagAllowed` check also returns false for reserved tags.

Verification passed: ESLint, 7 focused regression tests, and 324 existing topic, category, and post tests.