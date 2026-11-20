# Checkpoint

Implemented configurable filesystem completion for `:open`.

- Added `FilePathCategory` with favorites for an empty pattern, absolute path matching, `file:///` normalization, `~` expansion/contraction, safe handling of invalid paths, deterministic sorting, and three completion columns.
- Registered the category according to `completion.open_categories`; added `filesystem` to valid/default values and added `completion.favorite_paths` as an empty list of strings.
- Regenerated the settings help and updated existing completion expectations for the newly enabled empty category.
- Verification: `pytest -q tests/unit/completion/test_models.py tests/unit/config/test_configdata.py -k 'not benchmark'` passed (96 passed, 2 deselected).
