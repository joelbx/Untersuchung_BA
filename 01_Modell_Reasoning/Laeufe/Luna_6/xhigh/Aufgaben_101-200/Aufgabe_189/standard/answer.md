Implemented the module-level `extra_suffixes_workaround` with the Qt version gate, wildcard MIME expansion, and filtering of already supplied suffixes. `chooseFiles` now merges and deduplicates suffixes, then calls `super().chooseFiles(...)` once with the merged list as its third positional argument. Updated the existing tests to use the module helper and a `None` receiver.

The handler now always uses the superclass file picker; its previous external-picker branch was removed to meet the requested passthrough behavior.

Verification: `tests/unit/browser/webengine/test_webview.py` passed (20 tests), and `git diff --check` passed.