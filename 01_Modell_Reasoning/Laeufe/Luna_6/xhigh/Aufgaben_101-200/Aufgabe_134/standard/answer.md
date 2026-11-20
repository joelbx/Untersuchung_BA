Implemented Project Runeberg support. Work-search documents now include `id_project_runeberg` as an array, defaulting to `[]`; existing identifier aggregation remains unchanged. The search response also exposes the field.

Added [ProjectRunebergProvider](/app/openlibrary/book_providers.py:369) and the requested [read button](/app/openlibrary/templates/book_providers/runeberg_read_button.html:1) and [download options](/app/openlibrary/templates/book_providers/runeberg_download_options.html:1) templates.

Verification passed: 50 Solr updater and work-search tests, 4 tests in the full work-search directory, and `git diff --check`. Tests reported existing dependency deprecation warnings.