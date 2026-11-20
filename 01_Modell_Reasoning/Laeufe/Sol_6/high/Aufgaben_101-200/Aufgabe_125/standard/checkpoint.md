Task: implement topic backlinks feature in checked-out repository.
Status: complete.
Changes: Topics.syncBacklinks detects local and bare topic links, validates input, synchronizes per-post sorted sets and backlink events; creation/edit invoke synchronization. Topic timeline filters backlinks by topicBacklinks setting. Added default-off admin toggle, English strings, and regression tests.
Verification: mocha test/topicEvents.js test/posts.js test/topics.js (295 passing); ESLint on changed JavaScript files; git diff --check.
Constraints observed: local code/tests only; git history, index baseline, and harness configuration untouched.
