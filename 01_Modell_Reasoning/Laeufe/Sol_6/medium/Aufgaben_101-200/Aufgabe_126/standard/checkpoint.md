Task: Resolve assistant Markdown/HTML formatting and message-scoped embedded URL handling.
Status: Source changes complete. Focused assistant tests: 9/9 passed. Existing textToHtml, messageContent, and contentFromComposerMessage tests: 11/11 passed. Type check found only existing OpenPGP type conflict in packages/crypto/lib/worker/api.ts.
Changes: Threaded messageID from composer through preparation, rendering, and insertion; scoped URL restoration and preserved link/image formatting; corrected list nesting and Markdown conversion; added regression tests.
Constraints observed: Local code/tests only; no git history, index, or harness changes.
