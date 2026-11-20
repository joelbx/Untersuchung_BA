Fixed `format_languages` so language records resolve full names before the abbreviation fallback. “Irish” now returns `/languages/gle`, and the added regression test confirms that “Irish”, “Gaeilge”, and `ga` produce one entry.

All tests flagged by the reviewer pass: 12 language tests, 1 abbreviation helper test, and 101 catalog utility tests. No remaining failures.