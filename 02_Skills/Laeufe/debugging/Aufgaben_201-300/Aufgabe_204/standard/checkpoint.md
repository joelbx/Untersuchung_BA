# Contact date import checkpoint

Status: investigating root cause and existing date conventions before edits.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

## Root cause and pattern

CSV `getDateValue` only calls `date-fns/parseISO`; local Node reproduction shows `parseISO` rejects `Jun 9, 2022`, `2023/12/3`, and `03/12/1969`, whereas JavaScript `Date` accepts them. The vCard helper already parses text with `new Date(text)` but defaults invalid values to today. Serialization formats valid `Date` fields using `format(date, 'yyyyMMdd')`, so calendar dates should be constructed at local midnight for date-only ISO strings (the existing `parseISO` behavior). Git status was clean before changes. Hypothesis: an ISO-first parser with a JavaScript Date fallback will cover both formats while preserving existing ISO date semantics; returning undefined for invalid text avoids invented dates.

## Baseline regression check

Command: `yarn workspace @proton/shared test` (exit 1). Webpack reports missing `guessDateFromText` export, as expected before implementation. Karma then cannot start ChromeHeadless: `Can not find the binary /root/.cache/ms-playwright/chromium-1045/chrome-linux/chrome`. Browser tests cannot execute in this offline environment. I will use local static checks and a Node-based reproduction where possible, and keep browser-test uncertainty explicit.

## Result and verification

Implemented an ISO-first `guessDateFromText` with a JavaScript Date fallback, rejecting invalid ISO calendar strings that JavaScript would silently normalize. CSV and vCard text conversion now share it. Invalid text leaves the vCard helper result undefined; CSV retains the original text. Regression tests cover common formats, invalid input, existing Date identity, CSV conversion, and vCard serialization.

Checks:
- `yarn workspace @proton/shared check-types`: exit 0.
- `./node_modules/.bin/eslint packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts --quiet`: exit 0.
- `git diff --check`: exit 0.
- `/app/node_modules/.bin/karma start /tmp/shared-karma-system-chromium.cjs` with temporary system Chromium override and `--grep=/^property /`: exit 0, 12 success.
- Full suite with the same system Chromium override: exit 1, 872 success and 2 failures outside contacts (`toBase64` undefined file, cookie expiry). The shared test command itself still cannot execute its configured Playwright binary: `Can not find the binary /root/.cache/ms-playwright/chromium-1045/chrome-linux/chrome`; executing that binary directly reports `cannot execute: required file not found`. The available system Chromium runs the contact tests successfully.
