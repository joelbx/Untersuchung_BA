Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to normalize personal author names and import deduplicated alternate-script names from linked `880` fields for `100`, `700`, and `720` author entries. Added tests and updated affected expectations.

Verification: 132 tests passed; 1 existing expected failure.