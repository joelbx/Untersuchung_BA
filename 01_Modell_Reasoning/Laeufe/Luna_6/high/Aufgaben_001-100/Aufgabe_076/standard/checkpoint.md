# Checkpoint

Task: Resolve address parsing inconsistencies in `/app`.

Changes: Added exported `splitBySeparator` to `packages/shared/lib/mail/recipient.ts` to split on commas and semicolons, trim tokens, remove angle brackets, discard empty tokens, and preserve order. Updated `inputToRecipient` so a bracket-only address populates both `Name` and `Address` with the bare address while retaining named address parsing.

Validation: `yarn workspace @proton/shared test` compiled its webpack bundle, then could not start Karma because `/root/.cache/ms-playwright/chromium-1041/chrome-linux/chrome` is missing. `yarn workspace @proton/shared check-types` completed without reported errors. `git diff --check` completed cleanly.
