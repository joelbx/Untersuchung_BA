Task: Add filesystem path completion to :open.
Status: implemented FilePathCategory; integrated category ordering, favorite_paths configuration, and help; added filesystem completion tests and updated empty-category expectations.
Verification: tests/unit/completion/test_models.py and tests/unit/config/test_configdata.py passed (100 tests); git diff --check and py_compile passed.
Delegation: none.
