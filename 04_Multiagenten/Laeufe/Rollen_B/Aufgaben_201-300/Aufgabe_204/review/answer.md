VERDICT: FIX

**Code defect:** [guessDateFromText](/app/packages/shared/lib/contacts/property.ts:138) parses timezone-bearing ISO timestamps as instants, while [vCard serialization](/app/packages/shared/lib/contacts/vcard.ts:225) writes the local calendar day. In UTC, `2023-12-03T00:30:00+02:00` serializes as `20231202`. Preserve the supplied calendar day for contact date fields and cover an offset timestamp that crosses midnight.

**TEST_ENVIRONMENT_PROBLEM:** `yarn workspace @proton/shared test` exited 1: Webpack compiled, but Karma could not find its configured Playwright Chromium binary. Point the local runner to an installed Chromium binary and rerun. `yarn workspace @proton/shared check-types` exited 0.

I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). I did not change project code or tests.