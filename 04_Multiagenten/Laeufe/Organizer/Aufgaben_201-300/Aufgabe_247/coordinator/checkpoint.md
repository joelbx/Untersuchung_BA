Task: Resolve unauthorized getUpvoters access and cutoff/tooltip requirements.
Status: completed locally.
Changes: bulk topics:read validation for every post category with administrator bypass; single deduplicated username lookup retaining vote order; cutoff 6 response and tooltip handling with HTML and escaped usernames; added voting tests.
Verification: eslint on three changed JavaScript files passed; mocha test/posts.js --grep voting passed (12 passing); git diff --check passed.
Delegation: none.
