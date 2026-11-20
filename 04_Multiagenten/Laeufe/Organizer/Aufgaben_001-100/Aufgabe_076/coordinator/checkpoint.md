# Checkpoint

Task: Normalize address splitting and recipient conversion in /app.
Status: Complete. Added shared splitBySeparator, normalized recipient fields, updated both autocomplete paste paths, and added regression specs.
Verification: Shared and components TypeScript checks passed; targeted ESLint and Prettier checks passed; local Jasmine parsing specs passed (2 specs, 0 failures); git diff --check passed. Karma bundled successfully but could not launch because its configured Playwright Chromium binary is absent.
Delegation: None.
Constraints: Local repository only; no downloads; git history, index baseline, and harness configuration preserved.
