Resolved missing author fields in make_work with empty author inputs. Added requested type annotations, preserved supplied cover URL, and added regression tests for missing author fields and supplied metadata.
Verification: python -m pytest openlibrary/plugins/upstream/tests/test_addbook.py -q (13 passed).
