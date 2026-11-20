Task: repair contact import text date parsing and vCard consistency.
Implemented guessDateFromText and connected CSV and vCard conversion; unparseable values remain unset.
Added parsing and vCard serialization tests.
Validation: shared TypeScript check passed; Prettier check passed; Karma: 872 passed, 2 unrelated failures (cookie helper and toBase64 under system Chromium).
