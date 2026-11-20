Added the three missing translation keys to [en_EN.json](/app/src/i18n/strings/en_EN.json), resolving the review’s localization defect.

The reviewer’s exact Jest command passes: 4 suites, 10 tests. ESLint, stylelint, JSON validation, and `git diff --check` pass.

**TEST_ENVIRONMENT_PROBLEM:** Type checking still reports the same five errors in installed Matrix SDK typings and unrelated room settings files.