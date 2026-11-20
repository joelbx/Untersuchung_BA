Task: support version-aware modes for qt.workarounds.disable_accelerated_2d_canvas.
Status: complete. Updated the setting to always/auto/never (default auto), passed WebEngine context to the settings resolver, and added coverage for Qt 5, Qt 6.5/6.6, and Chromium version boundaries. Verified 113 qtargs tests and 31 configdata tests with QT_QPA_PLATFORM=offscreen; git diff --check passed.
