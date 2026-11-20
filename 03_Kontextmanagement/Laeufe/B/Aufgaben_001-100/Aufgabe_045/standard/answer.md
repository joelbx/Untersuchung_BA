Collection name validation is fixed. Both name segments must be valid Python identifiers and cannot be Python keywords. Dependency resolution uses the same validator, and the legacy helpers and their compatibility code are removed.

Verification passed: 70 collection loader tests, 30 galaxy install tests, and the keyword regression checks.