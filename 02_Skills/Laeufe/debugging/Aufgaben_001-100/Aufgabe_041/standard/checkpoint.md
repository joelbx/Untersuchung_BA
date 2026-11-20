# Checkpoint

Task: consolidate list functionality in `List`, including owner lookup and client registration.

Phase 1: investigating current definitions, imports, registrations, and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find`.

Phase 1 findings: `ListMixin` holds seed/export/preview methods; `core.models.List(Thing, ListMixin)` holds owner and mutations. `core.models` imports `ListMixin, Seed` at module load. `plugins.upstream.models.setup()` registers `ListChangeset`, and `plugins.openlibrary.lists` uses `ListMixin` only as a type annotation. Owner regex is prefix-only and restricted to `OL` numeric ids.

Phase 2 pattern: `core.models.register_models()` registers Thing subclasses; upstream `setup()` registers Changeset subclasses. `ListChangeset` inherits upstream `Changeset`, which supplies undo methods, so retain that inheritance while routing list-specific registration through `core.lists.model.register_models()`.

Phase 3 hypothesis: the fragmentation is caused by `ListMixin` inheritance and registrations living in unrelated functions. Moving mixin methods into `List`, replacing the annotation, and centralizing the two list registrations removes the split without changing `Thing` or `Changeset` inheritance.

Phase 4: Added focused tests before editing. `pytest -q openlibrary/tests/core/test_lists_model.py -k 'list_registration or list_owner_requires_complete_key'` failed as expected: `List` was absent from `core.lists.model`, and owner lookup returned None for `/people/alice/lists/example`. Removed `ListMixin` and moved its methods into `core.models.List`; list registration is now routed through `core.lists.model.register_models`, which registers `/type/list` and `lists`. `core.lists.model.List` resolves to the same `List` class through a lazy module attribute to avoid an import cycle. Updated the one `ListMixin` annotation.

Verification: `pytest -q openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_models.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/upstream/tests/test_models.py openlibrary/plugins/openlibrary/tests/test_lists.py -k 'not test_from_input_with_data'` passed: 26 passed, 1 deselected. `git diff --check` passed.

Broader check attempted: `pytest -q openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/openlibrary/tests/test_listapi.py` exited 1. `test_listapi.py` failed during collection with `ModuleNotFoundError: No module named 'cookielib'`; `TestListRecord.test_from_input_with_data` failed because `web.ctx.env` was absent (`AttributeError: 'ThreadedDict' object has no attribute 'env'`). Those checks remain unverified in this environment; both errors occur outside changed code.
