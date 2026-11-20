Implemented `guessDateFromText` to parse ISO and common JavaScript date formats, returning `undefined` when parsing fails. CSV import and vCard text conversion now use it; valid stored dates remain unchanged, and ISO date-only values preserve their calendar day when serialized.

- Updated [property.ts](/app/packages/shared/lib/contacts/property.ts:135) and [csvFormat.ts](/app/packages/shared/lib/contacts/helpers/csvFormat.ts:591).
- Type checking, targeted lint, and direct parser checks passed.
- The shared suite ran 868 tests: 866 passed; two unrelated existing failures occurred in the cookie helper and `toBase64` specs.