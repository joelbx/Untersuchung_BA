Removed `ListMixin` and consolidated list behavior, owner lookup, and `ListChangeset` in [core/lists/model.py](/app/openlibrary/core/lists/model.py). Its new `register_models()` registers `/type/list` and the `'lists'` changeset type. Older import paths remain available for existing callers.

Two delegated agents checked imports and tests; one updated [core/models.py](/app/openlibrary/core/models.py), and one added owner and registration coverage. The focused suite passed **23 tests**, and fresh-process checks passed for all three model import orders.

The wider list run passed 31 tests. One test failed because it lacks `web.ctx.env`; another could not collect because it imports Python 2’s `cookielib`. Those paths were untouched by this refactor.