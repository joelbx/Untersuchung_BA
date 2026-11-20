Implemented configurable reserved tag checks using `meta.config.systemTags`. Topic creation and editing now pass the user ID to validation, which rejects reserved tags for unprivileged users with the requested error. `isTagAllowed` returns false for reserved tags.

ESLint passed. The topic and category tests could not run because Redis is unavailable (`ECONNREFUSED 127.0.0.1:6379`).