# Checkpoint

Task: Restrict use of configurable system-reserved tags to privileged users.

Completed:
- Added `systemTags: []` to config defaults so the list is stored and loaded as an array.
- Tag validation checks normalized system tags and requires `user.isPrivileged(uid)`, returning `You can not use this system tag.` otherwise.
- Passed UID through topic creation, edit, and queued-topic validation.
- `isTagAllowed` rejects reserved system tags.

Verification:
- ESLint passed for modified JavaScript files.
- `install/data/defaults.json` parsed and `git diff --check` passed.
- `npx mocha test/topics.js test/categories.js`: 218 passing. The test run used a temporary local Redis process, which has been stopped.
