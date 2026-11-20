Fixed the IA import path so `London ; New York ; Paris : Berlitz Publishing` produces `publish_places: ["London", "New York", "Paris"]` and `publishers: ["Berlitz Publishing"]`. Added the requested parsing helpers and moved length based ISBN classification to `openlibrary.utils.isbn`.

The focused test suite passed: **37 tests**. `git diff --check` also passed.