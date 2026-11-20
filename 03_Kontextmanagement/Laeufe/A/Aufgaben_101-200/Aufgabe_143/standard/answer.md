Centralized author identifier generation in [catalog.utils](/app/openlibrary/catalog/utils/__init__.py) and made record expansion apply it to every author. Existing editions now supply name and birth/death dates for expansion to handle, without generating a separate identifier.

Relevant tests passed: 128 passed, 2 expected failures, and 1 expected pass. Ruff and `git diff --check` passed.