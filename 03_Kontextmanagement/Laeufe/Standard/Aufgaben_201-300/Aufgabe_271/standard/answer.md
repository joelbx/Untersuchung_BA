Fixed the IA import path so `London ; New York ; Paris : Berlitz Publishing` produces three `publish_places` and `["Berlitz Publishing"]` in `publishers`. Plain publisher names remain lists, and ISBNs are now classified in `openlibrary.utils.isbn` strictly by trimmed length.

The relevant tests pass: **54 passed**. `git diff --check` also passed.