Task: Gate the MIME-suffix workaround using runtime Qt only.
Status: Implemented and verified targeted behavior.
Changes: The workaround checks 6.2.3 and 6.7.0 with compiled=False. version_check documents runtime-only behavior and raises RuntimeError for compiled=True with exact=True. Tests cover mismatched runtime/compiled versions and both bounds.
Verification: 34 targeted tests passed; git diff --check passed. Full affected modules: 196 passed, 2 failed in unrelated Qt 6.9 QDataStream status count and QSaveFile warning tests.
