# Checkpoint

Task: Fix address token splitting and recipient normalization in `/app`.

Findings: The parser is `packages/shared/lib/mail/recipient.ts`. Its regex supports named recipients and bare inputs, but a bare bracketed address resulted in an empty `Name`. No existing recipient-specific test file is present.

Changes: Added exported `splitBySeparator`, which splits commas and semicolons, strips angle brackets, trims tokens, filters empty results, and preserves order. `inputToRecipient` now uses the parsed address as the name when the input has no display name, retaining named-recipient parsing.

Validation: `yarn workspace @proton/shared check-types` and `yarn workspace @proton/shared lint --no-cache` passed. `yarn workspace @proton/shared test --single-run` bundled successfully but could not launch Chrome because the configured Playwright Chromium binary is absent. No downloads were requested.
