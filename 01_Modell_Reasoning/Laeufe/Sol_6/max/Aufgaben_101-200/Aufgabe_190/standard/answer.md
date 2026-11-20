Added `preview=true` to the import and IA import endpoints. Preview runs the import pipeline with temporary keys and returns `preview: true`, proposed `edits`, and `cover_accepted`, without saving records, uploading covers, or updating Archive.org metadata.

Author matching now applies the requested name, date, and remote ID rules. Edition construction normalizes authors, descriptions, and languages; cover URLs use a case-insensitive host allowlist.

Verification: **246 add-book and import API tests passed**. Ruff and `git diff --check` passed.