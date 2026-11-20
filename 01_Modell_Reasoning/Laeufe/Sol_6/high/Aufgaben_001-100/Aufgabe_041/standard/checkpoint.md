# Checkpoint

Task: Remove `ListMixin`, consolidate list behavior in `core.models.List`, and register list documents and changesets through `core.lists.model.register_models`.
Status: Implemented and verified.
Changes: Moved mixin methods into `List`; broadened and anchored owner lookup; centralized list and list changeset registration; updated the list export type hint; added owner and registration tests.
Verification: 20 focused tests passed. `git diff --check` and Python compilation passed. Broader list suite has existing isolated failures: missing `web.ctx.env` in one test and unavailable `cookielib` in `test_listapi.py`.
