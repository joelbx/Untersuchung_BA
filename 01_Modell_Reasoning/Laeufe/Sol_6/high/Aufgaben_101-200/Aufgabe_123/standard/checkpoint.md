# Notification issue checkpoint

- Objective: render safe HTML in string notifications, secure notification links, and deduplicate non-success notifications by stable key.
- Status: implemented and verified.
- Changes: sanitize string notification HTML with a restricted tag/attribute set; secure all rendered notification anchors; use explicit key, string text, or identifier for non-success deduplication; render notification list by unique identifier so repeated successes remain distinct.
- Verification: focused Jest suite (4 tests) passed; components TypeScript check passed; ESLint on changed files passed; git diff --check passed.
- Constraints observed: local code/tests only; no git history, index baseline, or harness configuration changes.
