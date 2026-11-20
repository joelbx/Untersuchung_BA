Implemented the reported fixes across the frontend, backend utilities, routes, and templates. Notifications now load through `app.require` when opened, use the trigger element, and ignore stale responses. Quick search uses container `focusout` handling and clears stale results after navigation.

Also updated the fork/move category selectors, hash field normalization, email sender format, installer guard, post routes, admin dropdowns, merge search width, and recent chat links.

**Verification:** 102 existing tests passed. ESLint, Node syntax checks, and `git diff --check` passed. A temporary local Redis service was used for the tests and stopped afterward.