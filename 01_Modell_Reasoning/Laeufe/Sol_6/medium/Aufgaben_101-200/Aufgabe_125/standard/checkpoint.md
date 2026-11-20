Task: implement topic backlinks in the checked-out repository.
Status: implemented and verified. Added Topics.syncBacklinks, creation/edit hooks, event visibility gating, admin toggle, English localization, and focused tests.
Verification: mocha test/topics.js test/topicEvents.js (196 passing); ESLint on changed JS; git diff --check; JSON parse checks.
Constraints: local repository and existing tests only; preserve git history, index baseline, and harness configuration.
