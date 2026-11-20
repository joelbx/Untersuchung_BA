Implemented MARC contributor role support. `read_author_person` now maps recognized `$e` terms and `$4` codes to readable roles, with `$4` taking precedence. `new_work` preserves each role alongside its author in order and raises an exception when the edition and record author counts differ.

Updated the MARC expectations and added focused tests. All 158 relevant tests pass, and Ruff checks pass.