The Qt wrapper patch is ready for export. I corrected the initialization docstring and added a test confirming that checker errors display two blank lines at the end. The three reviewer test suites pass: 26, 6, and 19 tests.

The plain `--version` smoke check still aborts without a display (**TEST_ENVIRONMENT_PROBLEM**). It succeeds with Qt’s offscreen setting and the WebEngine sandbox disabled.