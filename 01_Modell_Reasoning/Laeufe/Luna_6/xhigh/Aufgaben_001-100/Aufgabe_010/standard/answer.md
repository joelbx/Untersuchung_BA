Implemented the composer and reply preview updates:

- Room replacement notices now use a semantic paragraph with the existing clear status text.
- Added a reusable, size configurable accessible [CancelButton](</app/src/components/views/buttons/Cancel.tsx>) and used it to cancel replies.
- Reply previews say “Replying to,” and sender profiles support inline rendering. Clickable profiles now support keyboard activation.

**Verification:** The MessageComposer Jest suite passed (3 tests); ESLint and Stylelint passed. `yarn lint:types` remains blocked by existing errors in `matrix-js-sdk` and two alias settings components; it reported no errors in changed files. Progress is recorded in `.codex-role-output/checkpoint.md`.