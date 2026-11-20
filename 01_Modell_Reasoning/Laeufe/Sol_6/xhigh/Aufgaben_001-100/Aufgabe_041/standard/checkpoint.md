# Checkpoint

Task: consolidate list behavior in `List`, remove `ListMixin`, and register list models.

Status: completed. `List`, `Seed`, and `ListChangeset` now live in the list model.
The list model's `register_models()` registers `/type/list` and `lists`.
Legacy `core.models.List`/`Seed` and `upstream.models.ListChangeset` imports remain available.

Validation: 19 model and engine tests passed, plus 7 list page tests;
Ruff and `git diff --check` passed.
The existing list page test `test_from_input_with_data` fails because its test
request has no `web.ctx.env`; `test_listapi.py` cannot collect on Python 3
because it imports `cookielib`.
