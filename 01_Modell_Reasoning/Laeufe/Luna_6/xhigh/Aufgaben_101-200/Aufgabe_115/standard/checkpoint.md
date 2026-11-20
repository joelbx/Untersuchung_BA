# Checkpoint: MARC contributor role support

- Added `ROLES` mappings for MARC relator codes, common full terms, abbreviations, and a common compound role.
- `read_author_person` now reads `$e` and `$4`, gives `$4` precedence, assigns only recognized mapped roles, and omits unrecognized roles.
- `new_work` aligns edition author keys with parsed MARC authors in order, carries each parsed role into the corresponding work author entry, and raises when author counts differ.
- Updated existing MARC expectation snapshots for canonical roles and omitted unrecognized role text.
- Verification: `python -m pytest openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/tests/test_add_book.py -q` passed (152 tests).
