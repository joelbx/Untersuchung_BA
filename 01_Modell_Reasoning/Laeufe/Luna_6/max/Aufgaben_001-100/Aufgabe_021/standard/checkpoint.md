# Checkpoint

Task: Add explicit and structured typing to the List and Seed model, normalize subject keys, and make seed/export handling safe across supported input forms.

Completed:
- Added `SeedDict`, `SeedSubjectString`, `SeedInput`, and an export result `TypedDict` in the core List model.
- Added subject prefix detection and pseudo key normalization; reused it in plugin request parsing and ListRecord conversion.
- Normalized seed keys for duplicate checks, add/remove, raw key lookup, and Seed construction. List seed retrieval resolves entity references and subject metadata.
- Made exports always contain `authors`, `works`, and `editions`, loaded records in each category, and filtered by their actual type.
- Added public method annotations to List and Seed, plus requested helper annotations and the related changeset `get_user()` annotation.
- Made missing request environment and missing default covers safe.

Verification:
- `compileall` and `git diff --check` succeeded.
- Focused existing tests: 20 passed (`test_model.py`, `test_lists_model.py`, plugin `test_lists.py`, and `test_helpers.py`).
- The separate legacy `test_listapi.py` module could not be collected because this Python environment does not provide `cookielib`.

Constraints followed: local repository code and tests only; no changes to git history, index baseline, or harness configuration.
