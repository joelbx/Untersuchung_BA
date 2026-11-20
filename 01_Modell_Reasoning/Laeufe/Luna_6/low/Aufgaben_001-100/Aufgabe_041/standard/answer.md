Consolidated list behavior into `List` in [model.py](/app/openlibrary/core/lists/model.py), removed `ListMixin`, and added `register_models()` for the list type and changeset. Updated core and upstream registration and the export type annotation.

`List.get_owner()` parses `/people/{username}/lists/{list_id}` and returns `None` when the key is invalid or the user cannot be resolved.

Verification: 16 targeted tests passed; `git diff --check` is clean.