Implemented Best Book Awards persistence and validation. Nominations require “Already Read” status and enforce uniqueness by user and work or topic. Added the authenticated add/update/remove API, the public count API, and Work award accessors.

Work redirects now count and update awards; account anonymization updates award usernames and reports the number changed.

Validation: 47 existing tests passed. Ruff, Python compilation, and `git diff --check` passed.

Key files: [bestbook.py](/app/openlibrary/core/bestbook.py), [api.py](/app/openlibrary/plugins/openlibrary/api.py), [models.py](/app/openlibrary/core/models.py), [schema.sql](/app/openlibrary/core/schema.sql).