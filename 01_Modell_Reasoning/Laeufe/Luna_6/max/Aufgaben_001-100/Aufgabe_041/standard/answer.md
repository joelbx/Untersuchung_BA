Removed `ListMixin` and moved its methods onto `List`. Owner lookup now parses list keys strictly and returns `None` for malformed keys or missing users. Added `core/lists/model.py` registration for `/type/list` and the `lists` changeset, and wired upstream setup to use it.

Verification: 23 relevant tests passed; one was excluded because `test_from_input_with_data` fails even in isolation when `web.ctx.env` is unset. Compilation and `git diff --check` passed.

Key changes: [List model](</app/openlibrary/core/models.py:963>), [list registration](</app/openlibrary/core/lists/model.py:22>), [upstream setup](</app/openlibrary/plugins/upstream/models.py:1044>).