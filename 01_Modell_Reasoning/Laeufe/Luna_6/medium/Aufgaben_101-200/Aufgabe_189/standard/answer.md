Implemented the module-level `extra_suffixes_workaround` and updated `chooseFiles` to pass a deduplicated union to the superclass. Updated tests to use the new helper and call the chooser with `None` as its receiver.

Focused verification passed: 14 tests. The full test module aborts during Qt application fixture setup in this environment.