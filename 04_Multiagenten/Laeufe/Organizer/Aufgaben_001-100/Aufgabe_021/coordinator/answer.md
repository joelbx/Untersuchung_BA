Updated the List and Seed model with explicit type annotations, a `SeedDict` type, and consistent key based handling for `Thing`, dictionary, and subject string seeds. Added subject key normalization and a subject string type guard. Exports now always contain `authors`, `works`, and `editions`, with fully loaded entries filtered by type.

**Validation:** 17 focused tests passed; targeted mypy, Ruff, and `git diff --check` passed. The legacy `test_listapi.py` could not collect because it imports Python 2’s `cookielib`.

No delegation was used, so there were no worker changes to adopt.