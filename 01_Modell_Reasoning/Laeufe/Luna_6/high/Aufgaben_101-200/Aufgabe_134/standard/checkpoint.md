# Checkpoint

Implemented the Project Runeberg work search identifier, provider registration, and the two public book provider templates.

- Work search fetches `id_project_runeberg` and `get_doc` emits it with `[]` as the missing-field default.
- Added `ProjectRunebergProvider` with substring-based OCAID detection and an open-access acquisition URL based on the edition's best Runeberg identifier.
- Added Runeberg download options and read button templates; the read button accepts optional analytics metadata and includes the provider toast.
- Updated the existing work search expectation for the newly consistent array field.

Verification: `pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py` passed (2 tests); `git diff --check` passed. Pytest reported only existing deprecation warnings.
