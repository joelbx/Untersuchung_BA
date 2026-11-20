VERDICT: FIX

[markdown.ts](/app/applications/mail/src/app/helpers/assistant/markdown.ts:52) normalizes list spacing inside indented code. In a local reproduction, `<pre><code>-   keep spaces</code></pre>` became `    - keep spaces`, changing literal code content. Restrict the cleanup to list lines outside code blocks.

Relevant tests passed:

- `yarn workspace proton-mail test --runInBand --coverage=false src/app/helpers/assistant/url.test.ts src/app/helpers/assistant/markdown.test.ts` — 2 suites, 9 tests passed.
- `yarn workspace proton-mail test --runInBand --coverage=false src/app/helpers/textToHtml.test.ts src/app/helpers/message/messageContent.test.ts src/app/helpers/composer/contentFromComposerMessage.test.ts` — 3 suites, 11 tests passed.

**TEST_ENVIRONMENT_PROBLEM:** `yarn workspace proton-mail check-types --pretty false` failed at unchanged [worker/api.ts](/app/packages/crypto/lib/worker/api.ts:579) because the installed `openpgp` and `pmcrypto` copies expose incompatible `PartialConfig` types. Align those dependency types to restore the type-check gate.

Review notes are in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code or tests were changed during review.