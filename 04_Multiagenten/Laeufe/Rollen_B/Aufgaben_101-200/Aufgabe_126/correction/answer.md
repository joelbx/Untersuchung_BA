Fixed the review finding in [markdown.ts](/app/applications/mail/src/app/helpers/assistant/markdown.ts): spacing cleanup now leaves indented code content unchanged. Added a regression test for the reported `<pre><code>` case.

Both exact test groups cited by the reviewer passed: 21 tests across 5 suites. `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** The type check still fails at unchanged [worker/api.ts](/app/packages/crypto/lib/worker/api.ts:579) because the installed `openpgp` and `pmcrypto` packages expose incompatible `PartialConfig` types.