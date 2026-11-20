Task: Expand MARC contributor role mapping and preserve author roles on new works.
Status: Complete. Added ROLES mapping, parsed $e/$4 with $4 precedence, carried roles to ordered work author associations, and enforced matching author counts. Updated MARC expectations and added focused tests.
Verification: 158 relevant tests passed; Ruff checks passed.
