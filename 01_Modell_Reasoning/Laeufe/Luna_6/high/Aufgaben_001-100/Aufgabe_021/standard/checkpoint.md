# Checkpoint

Task: improve type annotations and seed handling in the List model and related list utilities.

Implemented: `SeedDict` and `SeedSubjectString` types; subject key conversion and a type guard; normalized duplicate detection for add/remove/has; subject metadata resolution and Thing loading in seed access; all three export buckets with type filtering; explicit List/Seed method signatures; URL helper annotations.

Verification: final compileall and `git diff --check` passed. The focused model/list tests passed (9 passed with one known fixture failure deselected after its initial run: `TestListRecord.test_from_input_with_data` sees no `web.ctx.env`). `test_listapi.py` could not be collected because its legacy import `cookielib` is unavailable on Python 3.11.
