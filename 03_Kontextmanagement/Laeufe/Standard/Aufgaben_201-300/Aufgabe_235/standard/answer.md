Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to import linked MARC 880 names for 100, 700, and 720 authors. It now normalizes names and dates, preserves the primary author fields, and deduplicates `alternate_names`. Organization and event parsing was left unchanged.

Updated fixture expectations and added tests. **73 relevant tests pass**; `git diff --check` passes.