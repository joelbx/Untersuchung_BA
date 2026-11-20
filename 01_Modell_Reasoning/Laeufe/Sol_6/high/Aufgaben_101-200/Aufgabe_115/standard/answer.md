Expanded MARC contributor role support in [parse.py](/app/openlibrary/catalog/marc/parse.py): `ROLES` maps relator codes and common abbreviations to readable names. `read_author_person` reads `$e` and `$4`, gives `$4` precedence, and omits unrecognized roles.

Work author links now preserve roles in order and raise an exception when edition and record author counts differ. Updated MARC fixtures and added tests for parsing, precedence, ordering, and import.

**Verified:** 293 relevant tests passed; Ruff and `git diff --check` passed.