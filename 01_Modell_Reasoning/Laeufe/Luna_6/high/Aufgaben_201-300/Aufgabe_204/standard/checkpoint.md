# Checkpoint

Issue: Contact imports need reliable parsing of text dates while preserving calendar values through vCard serialization.

Implemented:
- Added `guessDateFromText` in `packages/shared/lib/contacts/property.ts`, validating JavaScript-parsed dates and returning `undefined` on failure.
- Updated CSV date conversion and vCard text-to-date conversion to use the shared parser.
- Invalid or missing vCard dates now remain unset instead of defaulting to today.
- Valid date fields continue through the existing vCard serializer, which emits `yyyyMMdd` from the Date's calendar fields.

Validation:
- Targeted ESLint passed for both changed TypeScript files.
- `git diff --check` passed.
- Shared test bundle compiled, but Karma could not start ChromeHeadless because the configured Playwright Chromium binary is missing.
- Shared `check-types` was invoked; it produced no diagnostics.
