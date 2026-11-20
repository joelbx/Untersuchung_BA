# Checkpoint

Issue: Contact import does not consistently parse text dates.

Plan: Inspect the shared contact property and CSV import conversion paths, add a robust text-to-Date parser, update vCard conversion while preserving valid Date inputs, verify date serialization behavior, then run relevant existing tests.

Implementation update: Added `guessDateFromText` in the shared contact property module. It uses date-fns ISO parsing first to preserve date-only calendar values during vCard serialization, then falls back to JavaScript `Date` parsing for common text formats. CSV date conversion and vCard text conversion now use the helper; valid stored dates are returned unchanged. Invalid CSV date text stays as text without a generated date.

Verification: `yarn workspace @proton/shared check-types` and targeted ESLint both passed. The shared Karma suite ran 868 tests: 866 passed; two unrelated failures remain in the cookie helper and `toBase64` specs. A direct check of the implemented parser passed for the requested ISO timestamp, month-name date, both slash formats, an ISO date-only value, and invalid text. `git diff --check` passed.
