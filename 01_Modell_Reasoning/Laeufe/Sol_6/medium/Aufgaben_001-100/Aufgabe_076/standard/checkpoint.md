# Checkpoint

Implemented exported splitBySeparator and normalized recipient Name/Address in packages/shared/lib/mail/recipient.ts.
Updated both address autocomplete paste handlers to use the shared splitter and discard empty segments.
Added packages/shared/test/mail/recipient.spec.ts.
Validation: shared and components TypeScript checks passed; targeted ESLint and git diff --check passed. Karma webpack compiled, but browser launch failed because the configured Playwright Chromium binary is incompatible with this environment.
