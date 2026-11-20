Task: add precise List/Seed typing and normalize seed handling.
Status: completed source edits and focused validation.
Changes: SeedDict and seed key normalization in model; subject key helpers and input normalization in plugin; export filtering and helper return types; focused tests.
Validation: 17 focused pytest tests passed; mypy on model/plugin passed; ruff check passed; git diff --check passed.
Limitation: test_listapi.py could not collect because local Python lacks legacy cookielib module.
