# Checkpoint

Task: implement reverse topic links.
Status: inspecting repository.
Findings: topic event metadata supports href/uid; create flows through Posts.create, edits through Posts.edit. Implement sync in Topics posts module; filter event reads by topicBacklinks.
Status: implemented and verified. Tests: mocha test/topicEvents.js (9 passing); eslint on changed JS files; git diff --check. Temporary Redis stopped.
