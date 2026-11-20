# Checkpoint

Issue: normalize address splitting and recipient conversion for comma/semicolon separated input, whitespace, angle brackets, and empty tokens.

Progress: added `splitBySeparator` to the shared recipient helper, updated both address autocomplete variants to use it for completed pasted entries, and made bracket-only recipient inputs use the bare address for both fields while preserving display-name parsing.

Validation: `AddressesEditor.test.tsx` passed (10 tests); shared and components TypeScript checks passed; `git diff --check` passed.

Complete: final diff reviewed. Changes are limited to the shared recipient helper and both address autocomplete variants.
