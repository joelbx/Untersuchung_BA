Implemented MARC role mapping and work author-role preservation.

- Added `ROLES` mappings and updated [`read_author_person`](</app/openlibrary/catalog/marc/parse.py:585>) to read `$e` and `$4`, prioritize `$4`, and omit unknown roles.
- Updated [`new_work`](</app/openlibrary/catalog/add_book/__init__.py:243>) to preserve author order and roles, and raise `ValueError` when author counts differ.
- Updated existing MARC expectations for mapped and omitted roles.

Verification: MARC parser tests passed (67), add-book tests passed (85), and Ruff passed.