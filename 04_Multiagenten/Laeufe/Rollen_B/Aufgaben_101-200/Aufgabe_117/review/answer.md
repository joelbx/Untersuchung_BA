VERDICT: FIX

**Code review:** I found no code defect in the locale setting or fallback logic in [configdata.yml](/app/qutebrowser/config/configdata.yml:314) and [qtargs.py](/app/qutebrowser/config/qtargs.py:211).

**TEST_ENVIRONMENT_PROBLEM:** `python -m pytest -q tests/unit/config/test_qtargs.py` aborted with exit 134 while pytest-qt created its application fixture without a display. The actionable correction for this headless environment is `QT_QPA_PLATFORM=offscreen`.

With that setting, `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py` passed **147 tests**, and `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_configdata.py` passed **31 tests**. `git diff --check` also passed. The verdict is FIX because a relevant test attempt was interrupted.