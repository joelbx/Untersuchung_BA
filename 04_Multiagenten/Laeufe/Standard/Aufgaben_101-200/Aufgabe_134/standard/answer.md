Implemented Project Runeberg support in the checked-out repository. Every indexed work document now has an `id_project_runeberg` array, including `[]` when no identifier exists. Search responses expose it while preserving the other identifier fields.

I added the registered [ProjectRunebergProvider](/app/openlibrary/book_providers.py), the [Read button](/app/openlibrary/templates/book_providers/runeberg_read_button.html) and [download options](/app/openlibrary/templates/book_providers/runeberg_download_options.html) templates, and included the field in the carousel’s search query.

Validation: 53 focused tests passed; both templates rendered; Ruff and `git diff --check` passed. The format-specific Runeberg download URLs could not be verified because external research is blocked.