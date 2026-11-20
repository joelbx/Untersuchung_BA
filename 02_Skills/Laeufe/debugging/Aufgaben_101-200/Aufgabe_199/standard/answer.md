Migrated `get_ia.py` to `requests`, including response status handling, UTF-8 fallback decoding, binary and text access, and Range headers. Updated the dependent `marc_subject.py` callers and added focused tests.

Verification: **95 relevant tests passed**, and `git diff --check` passed.