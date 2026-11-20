# MARC alternate-script author names

Status: implemented linked 880 alternate names for person fields 100, 700, and 720, normalized names and dates, and updated affected MARC expectations. `rg` is unavailable, so file searches used `grep` and `find`.

Checks: `git diff --check` passed. `python -m pytest openlibrary/catalog/marc/tests -q -o reruns=0` passed (124 tests; existing deprecation warnings).
