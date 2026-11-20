Task: Fix Qt 6.4 dark mode text threshold mapping.

Progress: Added a Qt 6.4 dark mode variant with ForegroundBrightnessThreshold for the text threshold, retaining the previous key for earlier versions. Added version-specific regression cases. The dark mode test module passed (43 tests) with QT_QPA_PLATFORM=offscreen. A plain pytest invocation aborted during Qt application initialization in the headless environment. Diff review and whitespace check completed.
