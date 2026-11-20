Removed `ListMixin` and moved its methods onto `List` in [core/models.py](/app/openlibrary/core/models.py:965). Owner lookup parses `/people/{username}/lists/{list_id}` and returns `None` for malformed keys or missing users.

Added `ListChangeset` and `register_models()` in [core/lists/model.py](/app/openlibrary/core/lists/model.py:150), registering `/type/list` and changeset kind `lists`. Updated upstream and list plugin references.

The focused model tests passed: **16 passed**. A broader test run also encountered an environment failure (`web.ctx.env` missing) and a collection error (`cookielib` unavailable under Python 3.11).