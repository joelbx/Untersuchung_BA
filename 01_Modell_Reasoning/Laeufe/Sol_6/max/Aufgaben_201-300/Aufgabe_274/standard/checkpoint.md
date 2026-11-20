# Checkpoint

Task: Support version-aware modes for `qt.workarounds.disable_accelerated_2d_canvas`.

Status: Complete. The setting is a string enum with `auto` as its default; QtWebEngine resolves `auto` using the Qt runtime and Chromium major version. Unknown Chromium versions now pass through feature processing without an assertion. Version, boundary, and resolver-context tests were added. `test_qtargs.py` and `test_configdata.py` passed together (146 tests); `git diff --check` passed.
