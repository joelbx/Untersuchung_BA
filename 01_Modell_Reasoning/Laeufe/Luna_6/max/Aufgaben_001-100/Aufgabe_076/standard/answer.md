Implemented address normalization in [recipient.ts](/app/packages/shared/lib/mail/recipient.ts:7): `splitBySeparator` trims tokens, removes angle brackets, filters empty entries, and preserves order. Bracket-only addresses now use the bare email for both recipient fields.

Both autocomplete variants use the helper when committing completed entries: [legacy](/app/packages/components/components/addressesAutomplete/AddressesAutocomplete.tsx:137) and [v2](/app/packages/components/components/v2/addressesAutomplete/AddressesAutocomplete.tsx:176).

Validation passed: `AddressesEditor.test.tsx` (10 tests), shared and components TypeScript checks, and `git diff --check`.