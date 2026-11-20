Fault localization complete.
- qutebrowser/config/configdata.yml:388 defines qt.workarounds.disable_accelerated_2d_canvas as Bool with default true; nearby enum settings at lines 280 and 330 show the String/valid_values pattern.
- qutebrowser/config/qtargs.py:276 calls _qtwebengine_settings_args without context, though _qtwebengine_args receives versions, namespace and special_flags. Lines 327-339 map Boolean values directly and perform no callable resolution.
- qutebrowser/qt/machinery.py exposes IS_QT6 for the runtime Qt check. qutebrowser/utils/version.py maps Qt 6.5 to Chromium 108 and Qt 6.6 to Chromium 112 and represents unknown Chromium major as None.
- tests/unit/config/test_qtargs.py:126 validates mapping keys against schema; this will fail if string keys are introduced without schema migration. Existing version_patcher fixture and Qt args tests provide a route for 5.15.2/6.5.3/6.6.0 boundary coverage. No current test directly covers this canvas workaround.
- Potential integration issue: _qtwebengine_features at qtargs.py:87 asserts Chromium major is known. An unknown Chromium version through the full qt_args path can fail before an auto resolver is reached; direct resolver testing can cover unknown unless that assertion is separately handled.
No project source or tests changed. No tests run in this localization-only pass.
