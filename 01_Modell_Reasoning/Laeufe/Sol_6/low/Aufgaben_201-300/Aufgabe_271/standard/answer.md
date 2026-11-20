Fixed the ImportAPI fallback for IA records without MARC. It now splits multiple locations from publisher names, and classifies trimmed ISBNs by length through `openlibrary.utils.isbn`.

Added regression tests for the reported publisher value and parser edge cases. All 24 focused tests passed; `git diff --check` passed.