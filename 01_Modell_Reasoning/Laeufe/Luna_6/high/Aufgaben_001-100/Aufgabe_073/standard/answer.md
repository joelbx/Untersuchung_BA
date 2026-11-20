Updated [vendors.py](/app/openlibrary/core/vendors.py) to serialize edition language display values, exclude “Original Language,” remove duplicates, and omit `languages` when the resulting list is empty. The metadata cleanup helper now preserves `languages`.

Validation: `python -m pytest openlibrary/tests/core/test_vendors.py -q` passed: 33 tests. There were 3 deprecation warnings.