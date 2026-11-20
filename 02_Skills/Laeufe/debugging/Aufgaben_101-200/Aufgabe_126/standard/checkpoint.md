# Checkpoint

Task: preserve assistant HTML formatting and scope embedded URLs to the originating message.

Root causes found locally: URL records lacked message identity; restoration accepted any known placeholder; composer/preview/insertion paths omitted message identity; HTML simplification stripped link/image formatting; Markdown cleanup destroyed list indentation and ordered markers; shared HTML converter disabled list parsing; cleanup altered code lines inside fences.

Patch: pass `modelMessage.localID` as `messageID` through assistant preparation, preview and insertion; store message identity and formatting with URLs; restore only matching placeholders and remove unknown links/images; preserve class/style; repair invalid nested lists; use structured Markdown list conversion and enable list rendering for assistant output while leaving shared defaults intact; keep fenced code alignment.

Verification: focused Jest suites for assistant URL/format conversion and composer content passed (13 tests). `git diff --check` passed.

Type check limitation: `node_modules/.bin/tsc --noEmit --project applications/mail/tsconfig.json --pretty false` exits 2 with an existing error at `packages/crypto/lib/worker/api.ts:579:77` (TS2345). It reports incompatible `PartialConfig` types from `/app/node_modules/openpgp/openpgp` and `/app/node_modules/pmcrypto/node_modules/openpgp/openpgp`, specifically `preferredHashAlgorithm` / `hash.md5`. No errors were reported in edited mail files. This prevents a clean full-project type-check claim.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); local grep/find used. No downloads or external research.
