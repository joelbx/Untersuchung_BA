# Fault localization checkpoint

Inspected `openlibrary/core/lists/model.py`, `openlibrary/plugins/openlibrary/lists.py`, relevant helpers, client loading, and existing list tests. Project source and tests remain unchanged.

Findings:
- `SeedDict` currently lives in the plugin (lists.py:27), while the model accepts untyped mixed seed forms. The client materializes stored references as `Thing` objects (`infogami/infobase/client.py:261-274`), but newly added seeds may remain dictionaries until reload.
- `List.add_seed`/`remove_seed`/`_index_of_seed` (model.py:68-104) compare mixed representations directly. `List._get_rawseeds` and `get_seeds` (109-116, 358-371) assume attribute access and do not resolve dictionary references. `Seed.__init__`/`document` (412-428) also assume non-strings have `.key`.
- `List.get_export_list` (218-253) dereferences `.type.key` on every stored seed and omits empty category keys. Its `get_many` results are used without type filtering. Related `get_book_keys`, `get_editions`, `get_all_editions` use similar assumptions.
- Subject normalization is duplicated in plugin `get_seed_info` and `lists_json.process_seeds` (112-118, 428-449), while `ListRecord.normalize_input_seed` (39-49) leaves string `/subjects/...` unnormalized and strips the prefix from dictionary form. Dedicated `subject_key_to_seed` and `is_seed_subject_string` helpers are absent.
- `urlsafe` and `_get_ol_base_url` have no annotations (helpers.py:221, models.py:44). `get_user()` is in `core/waitinglist.py:56` and currently has no return annotation.
- Existing targeted tests: 10 passed, 1 failed (`TestListRecord.test_from_input_with_data`), because test setup has no `web.ctx.env`; 3 reruns of that failure. Existing tests do not cover export or mixed representation duplicate handling.

Likely fix scope: establish `SeedDict` and a narrowed subject string type at the model boundary; normalize all input to key strings for comparisons; resolve references to `Thing` in `get_seeds`; preserve subject metadata and safe URL fallback; filter fully loaded export documents by type and return all three categories; reuse one subject pseudo-key normalization path in plugin ingestion. Confirm expected treatment of malformed or missing references as part of implementation.
