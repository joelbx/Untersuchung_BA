Implemented cover URL validation in [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py). Imports now process covers only from `ALLOWED_COVER_HOSTS`, matching hostnames case-insensitively for HTTP and HTTPS, and remove the `cover` key whether the URL is accepted or ignored.

Added helper tests for missing, unsupported, HTTP, and HTTPS cover URLs.

Verification: 82 add-book tests passed; `compileall` and `git diff --check` succeeded.