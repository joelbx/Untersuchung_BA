Fixed ImportAPI publisher parsing and ISBN classification.

- Publisher metadata now populates `publishers` and `publish_places` separately, including multiple locations and ordered publisher/place pairs.
- Added the requested edge case handling to the upstream parsing helpers.
- Moved ISBN length classification to `openlibrary.utils.isbn` and updated ImportAPI to import it there.

Validation passed: **35 focused tests**, plus `git diff --check`. The reported multi-location example was also checked manually.