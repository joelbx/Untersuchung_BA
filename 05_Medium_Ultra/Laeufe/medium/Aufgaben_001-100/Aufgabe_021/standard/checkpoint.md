Task: Add type annotations and simplify list seed handling.
Status: Implemented and verified.
Changes: Added SeedDict/SeedSubjectString typing, normalized key comparisons for seed membership, subject string helpers, safer subject URLs, complete type-filtered export categories, mixed-seed handling in list getters, and helper return annotations. Added regression tests.
Verification: 6 list-related pytest tests passed; ruff check and git diff --check passed.
