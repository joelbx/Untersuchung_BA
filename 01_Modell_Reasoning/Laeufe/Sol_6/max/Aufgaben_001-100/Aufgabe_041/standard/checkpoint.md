# List model refactor checkpoint

- Starting state: `/app` working tree has no reported changes.
- Task: consolidate list behavior in `List`, remove `ListMixin`, and register list and list changeset types.
- Completed: moved `List` methods and `ListChangeset` into `openlibrary/core/lists/model.py`, removed `ListMixin`, and added direct registration for `/type/list` and `lists`.
- Updated core registration, upstream alias, list API annotation, and owner parsing. Added tests for registration, owner resolution, and seed add/remove behavior.
- Verification: 29 focused tests passed with `web.ctx.env` initialized for list page tests. Ruff lint and `git diff --check` passed. Both import orders passed.
- Limitation: `test_listapi.py` cannot collect because `cookielib` is absent in this environment.
