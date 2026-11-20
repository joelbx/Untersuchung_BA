Updated collection name validation to reject Python keywords and require both FQCN segments to be valid Python identifiers. Dependency resolution now uses the same validator; the legacy helpers and their Python 2 fallback were removed.

- Collection loader tests: **57 passed** on Python 3.9.
- Galaxy collection tests: **43 passed** on Python 3.9.
- The default test run could not start Python 3.8 tests because pytest and PyYAML are missing there.
- Wrote the requested checkpoint to `.codex-role-output/checkpoint.md`.

Changed [\_collection_finder.py](/app/lib/ansible/utils/collection_loader/_collection_finder.py) and [dataclasses.py](/app/lib/ansible/galaxy/dependency_resolution/dataclasses.py).