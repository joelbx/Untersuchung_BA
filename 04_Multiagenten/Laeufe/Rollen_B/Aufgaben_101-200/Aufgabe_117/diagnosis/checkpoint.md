Fault-localization findings (2026-10-22):
- qutebrowser/config/qtargs.py:qt_args returns early for QtWebKit; _qtwebengine_args gets the pre-init WebEngine version and builds Chromium flags. There is no locale resource check or --lang workaround.
- qutebrowser/config/configdata.yml has Qt options and existing workaround definitions, but no qt.workarounds.locale setting. Add a Bool default false, backend QtWebEngine, restart true in an implementation pass.
- Likely helper location is qtargs.py; resource lookup should use Qt's translations directory/qtwebengine_locales and test the exact .pak path before overriding. Map Chromium locale aliases, then check mapped .pak, then base language, then en-US.
- Existing tests/unit/config/test_qtargs.py covers startup flags with mocked WebEngine versions but has no locale cases. Baseline: QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py => 117 passed. Plain pytest aborts while creating QApplication in this headless environment.
- No project source or tests changed. Uncertainty: exact Chromium alias ordering and Qt locale resource directory behavior need focused tests during implementation.
