Updated the Amazon import to include language names from edition metadata, exclude entries marked “Original Language,” remove duplicates, and omit `languages` when the resulting list is empty. The load cleaner now preserves the field.

Added tests for those cases. All 36 vendor tests pass.