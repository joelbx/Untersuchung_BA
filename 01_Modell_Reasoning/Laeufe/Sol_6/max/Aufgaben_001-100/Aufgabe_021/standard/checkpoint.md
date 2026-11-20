# Checkpoint

Task: Add List/Seed typing and consistent seed normalization.
Status: Complete.
Changes: Shared SeedDict, SeedSubjectString type guard and pseudo-key normalizer; normalized list membership and loaded seeds; fully loaded, type-filtered exports with all three groups; explicit List/Seed and URL helper annotations; focused regression tests.
Verification: 20 relevant pytest tests passed; mypy passed for five changed source modules (third-party import diagnostics disabled); ruff and git diff --check passed.
