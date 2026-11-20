Implemented MARC contributor role support.

- Added a broad `ROLES` mapping and `$e`/`$4` parsing with `$4` precedence; unknown roles are omitted from author records. See [parse.py](/app/openlibrary/catalog/marc/parse.py:34).
- Updated [new_work](/app/openlibrary/catalog/add_book/__init__.py:243) to preserve each author’s role in order and raise an exception when edition and record author counts differ.
- Updated existing MARC expectation snapshots for normalized roles.

Verification: the MARC parser and add book suites passed, **152 tests**.