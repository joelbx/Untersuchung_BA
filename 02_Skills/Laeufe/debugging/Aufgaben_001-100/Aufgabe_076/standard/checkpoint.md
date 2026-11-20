# Checkpoint

Task: normalize address splitting and recipient parsing.

Status: investigating root cause before editing parser code.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find.

Root cause: `inputToRecipient` matches a bracket-only address with an empty name and returns that empty capture. The two autocomplete paste handlers split on separators but only trim, so empty pieces and brackets survive. No shared `splitBySeparator` exists.

Pattern: plain input already maps Name and Address to the same trimmed string; both autocomplete versions duplicate the same paste split. Hypothesis: a shared normalizer for split tokens plus recipient normalization will cover the reported cases.

Failing test added at `packages/shared/test/mail/recipient.spec.ts`. Pre-fix Karma run from `/app/packages/shared` with `../../node_modules/.bin/karma start test/karma.conf.js --single-run` compiled it and warned that `splitBySeparator` is missing, then exited 1 because the configured Playwright Chromium binary `/root/.cache/ms-playwright/chromium-1041/chrome-linux/chrome` is absent. `/usr/bin/chromium` is present; will use a local process preload to point Karma at it without changing harness configuration.

Implementation: `splitBySeparator` is exported from `packages/shared/lib/mail/recipient.ts`; both autocomplete paste paths use it for completed tokens. `inputToRecipient` uses the parsed bare address for both fields. Added regression coverage in `packages/shared/test/mail/recipient.spec.ts`.

Verification:
- Pre-fix full Karma run with the local Chromium preload: 837 tests, 4 failures. The two new tests failed as expected (`splitBySeparator is not a function`; bracketed recipient Name was empty). The other two failures were cookie expiry and file toBase64.
- Post-fix command from `/app/packages/shared`: `NODE_OPTIONS='--require /tmp/codex-chromium-preload.js' ../../node_modules/.bin/karma start test/karma.conf.js --single-run` exited 1: 837 tests, 835 success, 2 failures. Both new address parsing tests passed. The remaining failures are the same cookie expiry and file toBase64 failures observed before the patch.
- `../../node_modules/.bin/tsc --noEmit -p tsconfig.json` passed in both `/app/packages/shared` and `/app/packages/components`.
- ESLint on changed files exited 0 with one existing deprecation warning for Input in legacy AddressesAutocomplete; Prettier check and `git diff --check` passed.

Uncertainty: full shared suite cannot pass in this Chromium environment due the two unrelated baseline failures. The configured Playwright Chromium binary is absent, so test runs used a local process preload pointing to installed `/usr/bin/chromium`; no repository harness configuration was changed.
