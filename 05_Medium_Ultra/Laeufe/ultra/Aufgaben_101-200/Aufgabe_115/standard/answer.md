Implemented MARC contributor role support in [parse.py](/app/openlibrary/catalog/marc/parse.py:36): `ROLES` maps MARC 21 codes and common abbreviations to readable names, and `read_author_person` reads `$e` and `$4`, gives `$4` precedence, and omits unrecognized roles.

Updated [work creation](/app/openlibrary/catalog/add_book/__init__.py:243) to keep roles paired with author keys in order and raise an exception when author counts differ. The path that adds authors to an existing work also preserves roles. Tests and MARC expectations were updated.

I delegated parser, work creation, and test changes to three agents, then reviewed the combined patch. **Verification:** 297 MARC and add-book tests passed; Ruff and `git diff --check` passed.