Fixed the IA import path. It now separates semicolon-separated locations into `publish_places`, keeps publisher names in `publishers`, and classifies ISBNs by trimmed length.

Updated [the import code](/app/openlibrary/plugins/importapi/code.py), [publisher parser](/app/openlibrary/plugins/upstream/utils.py), and [ISBN utility](/app/openlibrary/utils/isbn.py). Relevant tests pass: **69 passed**.