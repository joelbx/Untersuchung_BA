Moved the color interpolation helpers to [qtutils.py](/app/qutebrowser/utils/qtutils.py) and updated the download and tab progress indicators to use them. The existing color-space behavior is preserved, with percentage validation also covering a `None` color space.

Regression checks for both indicators pass. **342 relevant tests passed**, and `git diff --check` is clean.