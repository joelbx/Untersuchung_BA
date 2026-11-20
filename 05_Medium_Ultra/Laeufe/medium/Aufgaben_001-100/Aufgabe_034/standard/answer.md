Updated the IA importer to place ISBNs in `isbn_10` and `isbn_13`, and to split publisher names and publication places into `publishers` and `publish_places`. Added public utilities for both conversions and tests covering strings, mixed lists, whitespace, and empty inputs.

The relevant tests pass: **31 passed**. `git diff --check` also passed.