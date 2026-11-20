Implemented `override-validation` for `/import/api`. When true, it skips publication year, independent publisher, and required ISBN checks; the default preserves existing validation. Added case insensitive `is_promise_item(rec)`.

The existing import API and add-book suites passed: **74 tests**. `git diff --check` passed.

Changed: [code.py](/app/openlibrary/plugins/importapi/code.py:131), [add_book](/app/openlibrary/catalog/add_book/__init__.py:774), and [catalog utils](/app/openlibrary/catalog/utils/__init__.py:372). Checkpoint: [checkpoint.md](/app/.codex-role-output/checkpoint.md).