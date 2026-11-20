Implemented the composer accessibility and consistency updates:

- Room replacement notices now use a semantic status paragraph with the existing clear copy.
- Added a reusable, sized cancel button with accessible labels; applied it to reply preview and room search.
- Reply preview identifies the sender, and profile components support configurable HTML elements and keyboard activation when interactive.

**Verification:** Both relevant Jest suites passed (7 tests), as did ESLint, stylelint, and `git diff --check`. The full TypeScript check still reports five unrelated existing errors in the Matrix SDK and room settings components.