# Checkpoint

Task: expand MARC contributor role mapping and preserve roles in new works.
Status: complete.
Changes: normalized recognized $e and $4 roles; $4 takes precedence. New works preserve role and author order and reject mismatched author counts.
Verification: 165 relevant tests passed; Ruff and git diff --check passed.
