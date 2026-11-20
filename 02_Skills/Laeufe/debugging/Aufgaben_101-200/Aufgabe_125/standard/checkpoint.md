# Backlink feature checkpoint

Status: investigating repository structure, event flow, and post lifecycle before changes.

Constraints: local repository only; no downloads or external research. `rg` is unavailable (`/bin/bash: rg: command not found`), so using `find`/`grep`.

Root cause: topic events support typed timeline entries, but no backlink event type, reference extraction, lifecycle sync, or feature flag exists. Existing event link rendering already supports `href`; admin post settings use `data-field` and defaults.

Reproduction attempt: `./node_modules/.bin/mocha test/topicEvents.js --grep backlinks` failed before tests in the root `before all` hook with `connect ECONNREFUSED 127.0.0.1:6379` (exit 1). The integration suite cannot verify behavior without the configured Redis service. Will use isolated offline checks and preserve this uncertainty.

Implementation: added `Topics.syncBacklinks` in `src/topics/posts.js`, called from post creation and edit; added backlink topic event type, config gated timeline retrieval, default setting and admin switch, English source strings, and focused tests. Removed references purge only matching backlink event IDs and update `pid:{pid}:backlinks`.

Verification after patch:
- `node test/backlinks-offline.js` passed (exit 0): invalid input, full/bare links, duplicate/self/missing topic handling, additions/removals/idempotence, event metadata and config visibility.
- `./node_modules/.bin/eslint src/topics/posts.js src/topics/events.js src/posts/edit.js test/backlinks-offline.js test/topicEvents.js` passed (exit 0).
- `git diff --check` passed (exit 0).
- `./node_modules/.bin/mocha test/topicEvents.js --grep backlinks` failed in root setup, exit 1, `connect ECONNREFUSED 127.0.0.1:6379`; zero tests executed. Integration behavior remains unverified because local Redis is unavailable.
