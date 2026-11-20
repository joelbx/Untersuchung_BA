VERDICT: FIX
Code defect: applications/mail/src/app/helpers/assistant/markdown.ts:52 applies list-spacing cleanup to indented code. Reproduced with Turndown: <pre><code>-   keep spaces</code></pre> becomes Markdown "    -   keep spaces", then cleanup changes it to "    - keep spaces". Make normalization aware of code blocks so literal code spacing is retained.
Tests executed:
- yarn workspace proton-mail test --runInBand --coverage=false src/app/helpers/assistant/url.test.ts src/app/helpers/assistant/markdown.test.ts — PASS, 2 suites/9 tests.
- yarn workspace proton-mail test --runInBand --coverage=false src/app/helpers/textToHtml.test.ts src/app/helpers/message/messageContent.test.ts src/app/helpers/composer/contentFromComposerMessage.test.ts — PASS, 3 suites/11 tests.
TEST_ENVIRONMENT_PROBLEM: yarn workspace proton-mail check-types --pretty false — FAIL (exit 2) at unchanged packages/crypto/lib/worker/api.ts:579. TypeScript sees incompatible PartialConfig definitions from node_modules/openpgp and node_modules/pmcrypto/node_modules/openpgp. Align those dependency types to restore the type-check gate.
No project code or tests changed during review.
