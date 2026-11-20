# Checkpoint

Task: unify assistant upsell addon resolution and planIDs shape.
Status: implementation complete. Both new regression tests failed for the expected extra Mail Plus Scribe entry before the patch and passed afterward.
Constraints: use local files and tests only; do not alter git history, index baseline, or harness configuration.

Verification:
- `yarn workspace @proton/components test --runInBand hooks/assistant/assistantUpsellConfig.test.ts`: passed, 11 tests.
- `yarn workspace @proton/components test --runInBand`: passed, 144 suites and 1007 tests; 2 suites and 28 tests skipped.
- `yarn workspace @proton/components check-types`: failed (exit 2) at `../crypto/lib/worker/api.ts:577:77`, TS2345. Installed `openpgp` and `pmcrypto/node_modules/openpgp` expose incompatible `PartialConfig` / `preferredHashAlgorithm` types. This is outside the edited files; full type correctness remains unverified.
- `git diff --check`: passed.
