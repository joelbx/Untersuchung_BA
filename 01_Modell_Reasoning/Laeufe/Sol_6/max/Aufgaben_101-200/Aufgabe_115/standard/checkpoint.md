# MARC contributor roles

Status: implementation and verification complete.

Findings: `rec['authors']` retains parsed roles through `build_query`; `edition['authors']` contains resolved keys in the same order when `new_work` runs. Work author links support a `role` property.

Goal: map recognized relator terms and codes to readable roles, preserve author-role associations in new works, and verify with existing tests.

Verification: 297 MARC and add-book tests passed; Ruff lint and `git diff --check` passed. Ruff formatter check flags existing quote-style differences in touched files, so unrelated formatting was left unchanged.
