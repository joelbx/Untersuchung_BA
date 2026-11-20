# Import preview issue checkpoint

- Implemented `save` propagation through `load`, `load_data`, `new_work`, author handling, and the general, IA, and bulk MARC import paths.
- Preview mode now uses UUID based `/books/__new__…`, `/works/__new__…`, and `/authors/__new__…` keys, returns `preview: true` and proposed `edits`, and skips save calls, cover uploads, and Archive.org metadata updates.
- Added case insensitive exact hostname validation and exposed `cover_accepted` in preview responses.
- Added `author_import_record_to_author` and `import_record_to_edition` with compatibility aliases. Author normalization, name ordering, year matching, remote ID conflicts, descriptions, and language key conversion are handled through the shared conversion path.
- Verification: `compileall` and `git diff --check` passed. The existing import API, edition matching, and validation tests passed (97 tests). The wider add book run had 215 passing tests and four failures that assert legacy honorific retention or upload from a non-allowlisted cover host, contrary to the requested behavior.
