# Checkpoint

Implemented `isFromProton(element: Element): boolean` using `element.IsProton === 1`. Added optional `IsProton` typing to message metadata, conversations, and encrypted search messages. Added a `VerifiedBadge` component with a tooltip and reused it in the list column. Added helper tests for both element types and both flag values.

Checks:
- `./node_modules/.bin/jest --runInBand --config applications/mail/jest.config.js applications/mail/src/app/helpers/elements.test.ts`: passed (24 tests).
- `git diff --check`: passed.
- `./node_modules/.bin/tsc --noEmit --project applications/mail/tsconfig.json`: passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used filesystem search fallback.
