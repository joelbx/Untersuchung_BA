Updated [MARC author parsing](/app/openlibrary/catalog/marc/parse.py) to import linked 880 alternate-script names for 100, 700, and 720 authors. Added `name_from_list`, duplicate handling, and regression tests; organization and event parsing is unchanged.

Verification: all 124 MARC tests pass, and `git diff --check` passes.