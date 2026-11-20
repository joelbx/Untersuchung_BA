Task: Repair PassAliases drawer and bridge vault behavior.
Completed: extracted usePassAliasesSetup and provider helpers; made getDefault read-only and added createDefaultVault; added explicit No aliases state; updated bridge mock.
Verification: components TypeScript check passed; PassAliases Jest suite passed (3 tests); git diff --check passed.
