Expanded MARC contributor role mapping in [parse.py](/app/openlibrary/catalog/marc/parse.py). `read_author_person` now maps recognized `$e` terms and `$4` codes to readable roles, gives `$4` precedence, and omits unknown roles.

Updated [new_work](/app/openlibrary/catalog/add_book/__init__.py) to preserve each author’s role and order and raise an exception when the edition and import record author counts differ. Updated fixtures and added parsing and import tests.

Verification: 165 relevant tests passed; Ruff and `git diff --check` passed.