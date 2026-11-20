Implemented reserved system tags through `meta.config.systemTags`. Topic creation, editing, queueing, and the tag API now reject unprivileged use with “You can not use this system tag.” The `isTagAllowed` check also excludes reserved tags.

Validation passed: ESLint, 170 topic tests, and 6 tag whitelist tests. This work item is complete.