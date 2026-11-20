# Checkpoint

Task: Remove `ListMixin`, consolidate list behavior in `core.models.List`, and register list models through `core.lists.model.register_models`.
Status: Implemented. `List.get_owner` parses `/people/{username}/lists/{list_id}` and returns the site's user or `None`. Upstream list changeset and list view references updated.
Verification: 20 focused list engine/model/upstream model tests passed. `git diff --check` passed. Broader list tests have unrelated baseline setup issues (`cookielib` import and missing `web.ctx.env`).
