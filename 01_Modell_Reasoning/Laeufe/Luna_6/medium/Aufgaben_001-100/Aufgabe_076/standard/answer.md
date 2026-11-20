Implemented `splitBySeparator` in [recipient.ts](/app/packages/shared/lib/mail/recipient.ts), with comma/semicolon splitting, whitespace trimming, angle bracket removal, empty token filtering, and original order preserved. Standalone bracketed emails now produce matching bare values for `Name` and `Address`.

Validation passed: shared package lint, type check, and `git diff --check`.