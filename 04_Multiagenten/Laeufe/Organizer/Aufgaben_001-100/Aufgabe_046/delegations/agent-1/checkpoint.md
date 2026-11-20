# Python module dependency resolver

Status: implemented and verified.

Changes: queue-based module_utils traversal; explicit legacy and collection locator classes with candidate names; local-first legacy and redirect-first collection lookup; collection redirect shims, FQCN expansion, deprecation and tombstone handling; collection load diagnostic; package relative imports, synthetic intermediate package initializers, six normalization, and ansible base initializers.

Verification: `python -m pytest -q test/units/executor/module_common` passed (55 tests). `git diff --check` passed. Added focused tests for lookup order, redirects, routing metadata, package relative imports, missing collection diagnostics, and a 1,051-module dependency chain.
