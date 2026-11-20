# Checkpoint

Issue: JSDOM support for ModalTwo dialog content.

Status: complete.

Changes:
- Added a public forwardRef Dialog component. It uses native `<dialog>` when `showModal` and `close` are available and an accessible `<div role="dialog">` fallback otherwise, forwarding attributes, children, and the host ref.
- Switched ModalTwo to Dialog, passing its active open state and `aria-modal`.
- Added tests for accessible interactive children, prop/ref forwarding, and native/fallback hosts.

Verification:
- ModalTwo and Dialog Jest suites: 11 tests passed.
- Components TypeScript check: passed.
- ESLint on changed files: passed.
- Prettier check on changed files: passed.
- `git diff --check`: passed.
