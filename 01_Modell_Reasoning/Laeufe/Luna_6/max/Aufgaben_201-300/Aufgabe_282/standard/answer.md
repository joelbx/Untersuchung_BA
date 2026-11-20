Implemented JavaScript content filtering in [shared.py](/app/qutebrowser/browser/shared.py:171). Messages are shown only when their source and level are enabled and no matching source/message exclusion applies. Eligible UI messages use the requested format; other messages still go to the standard logger.

Added `.levels` and `.excludes` settings, with migration from the old setting, in [configdata.yml](/app/qutebrowser/config/configdata.yml:943). Updated the settings reference and changelog.

**Verification:** 38 focused tests passed; `git diff --check` passed. A broader run had one unrelated failure: `TestConfigPy.test_nul_bytes` expects `ValueError`, but Python 3.11 raises `SyntaxError`.