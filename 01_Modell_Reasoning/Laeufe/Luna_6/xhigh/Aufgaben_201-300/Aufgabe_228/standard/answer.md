Implemented Qt-native version parsing with normalized `QVersionNumber` values and migrated the Qt checks, distribution metadata, early initialization, and crash dialog comparison.

- Added `utils.parse_version()` and updated [qtutils.py](/app/qutebrowser/utils/qtutils.py), [earlyinit.py](/app/qutebrowser/misc/earlyinit.py), [version.py](/app/qutebrowser/utils/version.py), and [crashdialog.py](/app/qutebrowser/misc/crashdialog.py).
- Updated existing test fixtures for the new API.

**Verification:** 318 relevant utility, early-init, and crash-dialog tests passed; 19 distribution and sandbox tests passed. A broader `test_version.py` run exited nonzero during Qt/X11 teardown, so those affected cases were run separately.