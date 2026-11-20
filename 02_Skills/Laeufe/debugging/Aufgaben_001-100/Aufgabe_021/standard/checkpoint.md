# Checkpoint

Task: type List and Seed APIs, normalize subject seeds, and verify with local tests.
Phase: root cause investigation.
Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

Root cause: list input and API normalize subject paths differently; `List._index_of_seed` compares raw representations; `get_export_list` assumes every seed has `.type`, so a subject string raises AttributeError. Focused reproductions fail as expected (`pytest -q --reruns 0 ...`). `SeedDict` currently lives in the plugin, causing model typing to depend on the caller layer. Hypothesis: centralizing the seed type and normalizing key comparisons, then loading only valid Things for export, resolves these failures.

Implementation: centralized `SeedDict` and seed key extraction; normalized subject pseudo keys through a shared plugin helper; made export return all three buckets with loaded, type-filtered entities; annotated List, Seed and requested URL helpers; added regression tests. Export test exposed that MockSite returns `client.Thing` (the base class), so filtering now accepts that type. Updated `get_all_editions` query helper to consume `Seed.type` strings consistently.

Verification: `pytest -q --reruns 0 openlibrary/tests/core/test_lists_engine.py openlibrary/tests/core/lists/test_model.py openlibrary/tests/core/test_lists_model.py openlibrary/plugins/openlibrary/tests/test_lists.py` passed (15 tests). `git diff --check` passed. An AST check found no unannotated public List or Seed method arguments or returns.
