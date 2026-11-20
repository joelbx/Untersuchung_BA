Implemented the composer and related accessibility updates.

- Room replacement status now uses a semantic paragraph with clear text, and the replacement icon is marked decorative.
- Added a reusable, accessible [CancelButton](</app/src/components/views/buttons/Cancel.tsx>) with configurable sizing. Reply previews use it and say “Replying to.”
- Sender profiles can choose a wrapper element for different rendering contexts.
- Updated the composer test to check the paragraph and its text.

The composer tests, ESLint, Stylelint, and `git diff --check` pass. Type checking still reports five errors in Matrix SDK types and unrelated room settings files; none point to the modified files.