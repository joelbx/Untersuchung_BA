Implemented preview support for the import endpoints and added the requested `check_cover_url_host`, `author_import_record_to_author`, `import_record_to_edition`, and `load_author_import_records` interfaces, with compatibility aliases for the previous helper names.

Preview mode assigns placeholder keys and returns `preview: true` with an `edits` list. It skips record saves, cover uploads, and Archive.org metadata updates. Cover host checks now compare parsed hostnames case-insensitively.

Verification: compilation and `git diff --check` passed. The relevant add-book tests reported **119 passed and 3 failed**; the failures are existing author helper expectations around honorific normalization, which conflicts with the requested normalization behavior.