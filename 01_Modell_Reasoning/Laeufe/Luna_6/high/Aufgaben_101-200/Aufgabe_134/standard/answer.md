Implemented Project Runeberg support in work search and book providers.

- Work search now fetches and exposes `id_project_runeberg`, defaulting to `[]`.
- Added `ProjectRunebergProvider` with OCAID substring detection and open access acquisitions.
- Added Runeberg download options and read button templates, including optional analytics metadata and a provider toast.
- Updated the existing work search expectation.

Verification: `pytest -q openlibrary/plugins/worksearch/tests/test_worksearch.py` passed (2 tests), and `git diff --check` passed.