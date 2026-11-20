# MARC contributor roles

Issue: expand MARC contributor role mappings and preserve author roles when creating works.

Implemented `ROLES`, `$e`/`$4` precedence, omission of unknown roles, and role preservation with author count validation in `new_work`. Updated MARC expectations and added focused and import-flow tests. The MARC and add-book suites pass (290 tests). Ruff lint passes. Ruff's formatter defaults to double quotes and would rewrite whole files against this repository's existing style, so it was not applied.
