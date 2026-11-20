Implemented `preview=true` for the [import endpoints](/app/openlibrary/plugins/importapi/code.py). Preview runs the import pipeline, returns `preview`, `edits`, and cover acceptability with UUID placeholder keys, and skips saves, cover uploads, and Archive.org metadata updates.

The [import pipeline](/app/openlibrary/catalog/add_book/__init__.py) now validates cover hosts on both new and matched editions. The [author and edition conversion](/app/openlibrary/catalog/add_book/load_book.py) applies the requested name matching, language validation, and field normalization. I delegated those changes and the test audit to three agents, then integrated and verified the patch.

**Verification:** 242 relevant tests passed; Ruff and `git diff --check` passed.