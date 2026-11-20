I localized the role loss to two functions:

- [read_author_person](/app/openlibrary/catalog/marc/parse.py:432) copies `$e` as raw text and does not read `$4`. It needs a `ROLES` lookup, with `$4` taking precedence and unrecognized roles omitted.
- [new_work](/app/openlibrary/catalog/add_book/__init__.py:243) creates author references without roles. It needs to pair edition author keys with `rec['authors']` in order, preserve each mapped role, and raise an exception when the counts differ.

[import_author](/app/openlibrary/catalog/add_book/load_book.py:271) drops role data while building edition authors, so `rec['authors']` is the available source when creating a work. One uncertainty is the existing edition path, which can supply authors that differ from the incoming record. Existing MARC fixture expectations contain raw abbreviations and would need review.

This diagnostic pass changed no project source or tests, as required by the specialist instructions.