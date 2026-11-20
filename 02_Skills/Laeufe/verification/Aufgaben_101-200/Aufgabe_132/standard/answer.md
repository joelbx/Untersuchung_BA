Added a configurable `systemTags` setting and enforced it when users create or edit topics, submit queued topics, or add tags through the API. Unprivileged users receive “You can not use this system tag.” The `isTagAllowed` check also rejects reserved tags.

Verification: the topic, category, and post suites passed (318 tests); ESLint and `git diff --check` passed.