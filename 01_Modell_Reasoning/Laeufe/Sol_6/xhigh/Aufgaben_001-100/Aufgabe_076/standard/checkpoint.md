# Address parsing fix checkpoint

- Objective: normalize separated address input and bracketed recipient tokens.
- Status: implemented shared separator parser, corrected bracketed recipient names, and updated both autocomplete callers.
- Verification: targeted Jasmine regression specs pass (3 specs); full shared Karma suite bundles but cannot launch its configured Playwright Chromium binary. Shared and component type checks, formatting, and targeted ESLint pass.
- Status: implementation and verification complete.
- Constraints: use repository code and existing tests only; leave git history, index, and harness configuration untouched.
