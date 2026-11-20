# Contact date import checkpoint

- Issue: parse common text dates for CSV and vCard contacts, preserve intended calendar dates on vCard serialization.
- Repository initially clean; no AGENTS.md found.
- Implemented `guessDateFromText`, wired CSV and vCard date conversion, and kept invalid dates unset.
- Added parser and CSV-to-vCard serialization coverage.
- Verification: shared TypeScript check passed; Prettier and diff checks passed; filtered Karma contact tests passed (14/14).
- Full shared Karma suite: 871/873 passed; unrelated cookie expiry and empty-file base64 tests failed in system Chromium.
