Fixed IA imports so publisher metadata such as `London ; New York ; Paris : Berlitz Publishing` produces ordered `publish_places` and a publisher-only `publishers` list. ISBNs are now trimmed and classified by length using the utility in [isbn.py](/app/openlibrary/utils/isbn.py).

The relevant tests pass: **34 passed**. `git diff --check` is clean. I solved this directly; no delegation was used.