Fixed the IA import path. It now separates multiple publication places from publisher names, preserves plain publisher values as a list, and classifies trimmed ISBNs by length using `openlibrary.utils.isbn`.

Verification: 59 relevant tests passed.