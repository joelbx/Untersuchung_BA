Task: Expand MARC contributor role mapping and preserve author-role associations on new works.
Status: Complete. Added ROLES mapping for MARC codes and common abbreviations, $4 precedence over $e, and ordered work author roles with count validation. Updated parser fixtures and added focused parser/work/import tests.
Verification: 164 relevant tests passed; ruff check and git diff --check passed.
Constraints: Used local repository and existing tests only; no git history/index/harness changes.
