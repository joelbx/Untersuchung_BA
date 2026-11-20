# Checkpoint

Task: implement IDN-to-Punycode URL handling and hostname extraction, update external link handling, and run relevant existing tests.

Findings: `punycode.js` is already a component dependency. The existing link handler's encoder operated on URL path segments and could also return browser-dependent output, while helper coverage exists in `packages/components/helpers/url.test.ts`.

Completed: added hostname extraction and hostname-only Punycode conversion helpers; updated external-link confirmation to use the converted URL and show an error when link extraction fails.

Validation: the existing URL helper test passes (11 tests), the components type check passes, ESLint passes for both changed source files, and `git diff --check` passes.
