# Checkpoint

Task: expand MARC author/contributor role handling and preserve author-role associations when creating works.

Completed:
- Added `ROLES` mappings for MARC relator codes, descriptive role terms, and common abbreviations.
- `read_author_person` reads `$e` and `$4`; `$4` takes precedence. Recognized values are converted to display names, while unknown or missing roles are omitted.
- `new_work` pairs work author entries with MARC author records in input order, copies each available role, and raises `ValueError` if the author counts differ.
- Updated existing MARC XML and binary expectations for canonical role values and omitted unknown roles.

Verification:
- `python -m pytest openlibrary/catalog/marc/tests/test_parse.py -q`: 67 passed.
- `python -m pytest openlibrary/catalog/add_book/tests/test_add_book.py -q`: 85 passed.
- `python -m ruff check openlibrary/catalog/marc/parse.py openlibrary/catalog/add_book/__init__.py`: passed.
