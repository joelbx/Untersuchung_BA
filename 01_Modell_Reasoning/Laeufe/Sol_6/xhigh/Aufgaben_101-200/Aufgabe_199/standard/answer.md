Migrated [get_ia.py](/app/openlibrary/catalog/get_ia.py) from urllib to requests, including response validation, retry handling, UTF-8 default decoding, and `.content`/`.text` reads. Updated the shared helper’s callers in [marc_subject.py](/app/openlibrary/catalog/marc/marc_subject.py) and added focused tests.

Verification: 97 relevant tests passed; `git diff --check` passed.