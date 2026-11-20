Implemented topic backlinks. New and edited posts now synchronize topic references, add or remove backlink events, and maintain each post’s backlink set. The timeline uses `[[topic:backlink]]`, links to the referencing post, and shows backlinks only when the new admin setting is enabled.

Verification: 110 topic event and post tests passed; ESLint and `git diff --check` passed.