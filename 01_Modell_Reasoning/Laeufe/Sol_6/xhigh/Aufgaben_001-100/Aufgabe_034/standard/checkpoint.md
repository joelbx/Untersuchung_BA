Task: Normalize Internet Archive ISBN and publisher metadata for Open Library editions.

Status: Implemented public ISBN and publisher/place utilities in `openlibrary/plugins/upstream/utils.py` and integrated them into `get_ia_record`. Updated existing expectations and added cases for single and mixed ISBNs, publisher lists, whitespace, and empty values. Relevant pytest suite passed (34 tests); flake8 and `git diff --check` passed.
