Implemented import preview mode across the general and IA endpoints, including bulk MARC imports. Preview returns proposed edits with UUID based placeholder keys and reports cover acceptance without saving records, uploading covers, or updating Archive.org metadata.

Added case insensitive cover host validation and the renamed author and edition conversion functions. These normalize author names, compare dates by year, and convert descriptions and language fields.

Verification: syntax and diff checks passed; 97 import API, matching, and validation tests passed. The wider add book run had four failures tied to legacy expectations for retained honorifics and uploads from a disallowed cover host.

Core changes are in [add_book](</app/openlibrary/catalog/add_book/__init__.py:218>), [load_book.py](/app/openlibrary/catalog/add_book/load_book.py:299), and [importapi/code.py](/app/openlibrary/plugins/importapi/code.py:179).