# Checkpoint

Task: Consolidate list functionality by removing `ListMixin`, placing owner lookup on `List`, and registering `List` and `ListChangeset` through `register_models` in `openlibrary/core/lists/model.py`.

Completed: Moved list behavior and the `List` class into `openlibrary/core/lists/model.py`, replaced `ListMixin` use with `List`, routed list thing and changeset registration through `openlibrary.core.lists.model.register_models`, and removed the duplicate upstream changeset registration.

Verification: `pytest -q openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_models.py openlibrary/plugins/upstream/tests/test_models.py` passed (16 tests). The broader existing list plugin run is blocked by unrelated baseline issues: `test_lists.py::TestListRecord::test_from_input_with_data` lacks `web.ctx.env`, and collecting `test_listapi.py` fails because `cookielib` is unavailable.
