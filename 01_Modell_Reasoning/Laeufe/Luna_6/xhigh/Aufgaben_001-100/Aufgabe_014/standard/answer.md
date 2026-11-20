Implemented the requested fixes across notification loading, quick search, fork/move and merge modals, hash utilities, email formatting, install guards, post routes, admin dropdowns, and recent chat links.

Notifications now load through `app.require`, refresh when opened, and ignore stale responses. Quick search uses focus-container events and clears stale results after navigation. Fork and move selectors use a cached element with `dropup`.

**Verification:** ESLint and `git diff --check` pass. Existing database/hash and emailer tests passed (71); search and notification tests passed (43). The temporary Redis test server has been stopped. Pre-existing untracked `appendonlydir/` was left untouched.