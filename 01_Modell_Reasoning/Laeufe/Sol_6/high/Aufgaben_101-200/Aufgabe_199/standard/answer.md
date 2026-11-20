Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from urllib to requests, including retries, status handling, charset defaults, binary and text responses, XML parsing, and range requests. Updated its Response-based caller in [marc_subject.py](/app/openlibrary/catalog/marc/marc_subject.py) and added focused tests.

Verification: all 63 catalog tests pass; `git diff --check` passes.