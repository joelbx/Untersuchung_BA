Implemented the `chat:privileged` gate across chat checks. Users without it now receive `[[error:no-privileges]]` when starting a chat with or inviting a privileged user. Profiles expose `canChat`, and the privilege label and OpenAPI schema are updated.

Verification passed: 77 messaging tests, ESLint, and `git diff --check`. The repository issue is complete.