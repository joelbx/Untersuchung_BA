Amazon imports now include unique, human-readable language names from edition metadata. Entries marked “Original Language” are excluded, and `serialize` omits `languages` when the resulting list is empty. The load cleaner also preserves the field.

The vendor test suite passes: **36 tests**.