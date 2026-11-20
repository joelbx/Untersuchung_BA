# Checkpoint

Task: clean local uploaded group and user cover/avatar files on explicit removal and account deletion.
Status: implemented and verified.
Changes: group cover and thumbnail cleanup, user cover/avatar cleanup with safe local URL mapping, account deletion cleanup, socket delegation, and disk-level regression tests.
Verification: 340 passing in test/image-cleanup.js, test/user.js, and test/groups.js; ESLint clean; git diff --check clean.
