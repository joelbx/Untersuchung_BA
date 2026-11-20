Correction round result: The existing QColor-to-QSS implementation and its four utility cases were sound. In tabwidget.py, converted favicon QSize and QPoint coordinates to integers because installed PyQt5 rejects floats, allowing the tab widget suite to execute.

Exact reviewer commands rerun:
- python -m pytest -q tests/unit/utils/test_qtutils.py: startup fails on deprecated pytest.ini --strict.
- QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/mainwindow/test_tabwidget.py: same startup failure.
- QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts='' tests/unit/utils/test_qtutils.py: 123 passed, exit 0.
- QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts='' tests/unit/mainwindow/test_tabwidget.py: 18 passed, then interpreter aborts during shutdown in pre-existing objreg.delete with RegistryUnavailableError('window'), exit 134.
- The tab widget subset excluding benchmarks likewise reports 9 passed, then aborts in the same shutdown path.

git diff --check passes. Remaining test exit is a test environment / Qt teardown problem; no harness or pytest configuration was changed.
