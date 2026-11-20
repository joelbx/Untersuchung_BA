# Import preview checkpoint

Task: add non-persistent preview to import endpoints, expose edits, and align cover, author, and edition validation.

Initial findings: core pipeline is in `openlibrary/catalog/add_book/__init__.py` and author/edition conversion in `load_book.py`; endpoints are in `openlibrary/plugins/importapi/code.py`. Existing tests are under each module's `tests` directory. Working tree was clean at start.

Next: inspect all write paths, implement save propagation and preview response, then run relevant existing tests.

Implemented: save propagation through new and matched import paths, UUID preview keys and edits, cover host validation and acceptance reporting, renamed conversion interfaces, and endpoint preview parameters. Added focused tests and updated the old matched-cover test to use an allowed host.

Verification: 131 relevant pytest tests passed; Ruff and git diff --check passed.
