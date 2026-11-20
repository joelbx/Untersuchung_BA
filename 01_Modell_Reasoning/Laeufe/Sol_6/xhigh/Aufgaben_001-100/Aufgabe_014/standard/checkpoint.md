# Checkpoint

Task: Resolve the NodeBB v4.4.3 dropdown, quick search, hash, email, installation, route, and template issues.

Status: Complete. Notifications load through app.require from the dropdown trigger and ignore stale responses. Fork and move selectors use dropup. Quick search uses focusout, resets on navigation, and ignores stale responses. Mongo and Redis hash fields, outbound email sender, installer guard, post redirection routes, admin dropdown scrolling, merge search width, and recent chat room link are updated.

Verification: ESLint passed on changed JavaScript. Existing hash, notification, and email suites passed (102 tests). Hash suite with the new numeric field regression test passed (66 tests). Existing post redirect tests passed (3 tests). git diff --check passed. Local Redis used for tests was stopped.

Constraints: Used local code and tests only; did not alter git history, index baseline, or harness configuration.
