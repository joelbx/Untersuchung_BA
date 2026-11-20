Resolved the IA metadata import issue. `get_ia_record` now emits separate ISBN-10 and ISBN-13 lists and separates publisher names from publication places. It omits empty normalized fields while preserving the other metadata mappings.

The relevant existing tests passed (**24 tests**), and `git diff --check` passed.