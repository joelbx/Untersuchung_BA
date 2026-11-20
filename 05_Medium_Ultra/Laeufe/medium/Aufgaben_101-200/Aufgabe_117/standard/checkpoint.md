Task: Fix QtWebEngine 5.15.3 locale fallback for missing locale .pak files.
Status: Complete. Added QtWebEngine-only qt.workarounds.locale (default false), locale path and Chromium fallback helpers, and conditional --lang startup argument. Added focused locale, gating, integration, and config schema tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py: 182 passed. git diff --check passed.
Constraint note: First pytest run aborted at Qt application setup without a display; offscreen rerun passed. flake8 is not installed locally.
