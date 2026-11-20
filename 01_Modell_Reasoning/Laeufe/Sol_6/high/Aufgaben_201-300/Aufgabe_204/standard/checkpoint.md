Task: Resolve contact import parsing for common text dates.
Status: Implemented shared date parsing for ISO, month-name, and slash formats; CSV and vCard date conversion now use it. Invalid text stays unset in the date helper, and CSV keeps invalid text as text. Added parsing and serialization regression tests.
Verification: Focused Karma property run passed (27 tests); TypeScript check, ESLint, Prettier, and git diff check passed. Full shared Karma suite ran 875 tests: 873 passed, with two unrelated existing browser failures in toBase64 and cookie expiry.
Constraints: Use local repository only; preserve calendar values and invalid dates as unset.
