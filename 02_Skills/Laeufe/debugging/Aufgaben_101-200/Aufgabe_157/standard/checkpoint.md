# Mail metrics helper checkpoint

- Task: standardize mailbox metric label IDs and page size strings, and add the mail app's metrics dependency.
- Status: investigating existing enums, helpers, and dependency metadata before editing.
- Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find` locally.

## Investigation and hypothesis

- Root cause: the requested metrics normalization interface does not exist. Existing label logic exposes `isCustomLabelOrFolder`, backed by `MAILBOX_LABEL_IDS`; page sizes are numeric enum members 50, 100, 200. Directly stringifying missing or unsupported values would yield nonstandard metric labels.
- Pattern: `applications/mail/src/app/helpers/labels.ts` is the existing built-in/custom discriminator; `packages/shared/lib/mail/mailSettings.ts` defines the supported sizes. Other app manifests use `"@proton/metrics": "workspace:^"`; the package is already present as a workspace lock entry, but the `proton-mail` lock entry lacks the dependency.
- Hypothesis: using the existing predicate and an explicit enum switch with a 50 default will produce the required labels. Focused tests cover all enum values, missing settings, unsupported values, and built-in/custom IDs.

## Resolution and verification

- Added `applications/mail/src/app/metrics/mailMetricsHelper.ts` with `getLabelID` using the established custom-label predicate and `getPageSizeString` mapping supported enum values with a `50` fallback.
- Added `@proton/metrics` as a workspace dependency in the mail manifest and its `proton-mail` yarn lock entry.
- Focused test before implementation failed as expected: Jest could not resolve `./mailMetricsHelper`.
- Final checks passed: `./node_modules/.bin/tsc --noEmit --project applications/mail/tsconfig.json --pretty false`; targeted Jest run for the new helper plus existing labels and paging suites (43 tests); ESLint for the new files; `git diff --check`.
