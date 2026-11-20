Task: Expose `id_project_runeberg` as an array in every work search document, and add Project Runeberg acquisition provider and templates.

Status: Implemented Runeberg indexing/search field, provider registration, acquisitions, and read/download templates. `rg` was unavailable, so local inspection used `find` and `grep`.

Checks:
- `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py openlibrary/plugins/worksearch/schemes/tests/test_works.py openlibrary/tests/solr/updater/test_work.py openlibrary/tests/solr/updater/test_edition.py openlibrary/tests/test_runeberg_provider.py -q` — 85 passed.
- Both new templates compiled and rendered locally with representative `runeberg_id`.
- `git diff --check` — passed.

Uncertainty: External Project Runeberg format links could not be verified because external research is prohibited. The download template uses the catalog's `download.pl` URL with format-specific `mode` parameters. The canonical edition page is used for reading and acquisition.
