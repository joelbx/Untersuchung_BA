Implemented `expand_record()` in [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py). Updated add-book callers, merge comparison documentation, and tests; removed the old helper from `merge_marc.py`. Added coverage for combining ISBNs, copying comparison fields, and filtering sentinel values.

Relevant tests passed: **9 passed, 2 xfailed**. `git diff --check` passed.