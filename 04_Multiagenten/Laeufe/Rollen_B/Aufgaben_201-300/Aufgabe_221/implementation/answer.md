Implemented Best Book Awards backend support: nomination storage with read and uniqueness checks, add/update/remove and count JSON endpoints, Work accessors, and award updates during work redirects and account anonymization. Redirect collisions keep the destination nomination.

The focused test suite passed (45 tests). Ruff and `git diff --check` also passed.