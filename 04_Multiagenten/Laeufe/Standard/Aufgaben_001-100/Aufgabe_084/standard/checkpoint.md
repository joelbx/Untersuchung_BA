Task: Add public removeTechnicalFields to EntityUtils for new entity copies.
Status: Complete. Function recursively deletes keys beginning _finalEncrypted, _defaultEncrypted, or _errors from entity and nested objects/arrays, mutating in place. Added tests for unchanged entities and nested removal.
Verification: TypeScript type check passed; full built test suite passed on rerun (8680 assertions). First run had one unrelated ConfigFileTest 500ms timing failure. git diff --check passed.
