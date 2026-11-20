# Checkpoint

Task: Resolve the list model refactor in `/app`.

Completed:
- Moved all `ListMixin` methods onto `core.models.List` and removed `ListMixin` references.
- Added strict owner-key parsing for `/people/{username}/lists/{list_id}`; malformed keys and missing users resolve to `None`.
- Added `core.lists.model.register_models()` for `/type/list` and the `lists` changeset registration, and wired upstream setup through it.
- Updated list export typing to reference `List`.

Verification:
- `py_compile` passed for changed Python modules.
- Relevant pytest selection: 23 passed, 1 deselected.
- The deselected test (`test_from_input_with_data`) fails even in isolation because it accesses `web.ctx.env` when no request context is initialized; this is unrelated to the model refactor.
