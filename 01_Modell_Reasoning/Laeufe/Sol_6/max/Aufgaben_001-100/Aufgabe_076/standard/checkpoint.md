# Address parsing issue checkpoint

- Added `splitBySeparator` in the shared mail recipient module and made bare bracketed emails populate both recipient fields.
- Updated both address autocomplete paste handlers to discard empty segments while retaining display names for named recipients.
- Added focused shared mail tests for separator, bracket, and recipient cases.
- The shared Karma suite bundled successfully but could not start its configured Playwright Chromium binary (missing locally).
- Focused recipient specs passed with the repository's installed Jest transformer (4 tests).
- Shared and components TypeScript checks passed. ESLint and Prettier checks passed for all changed files.
