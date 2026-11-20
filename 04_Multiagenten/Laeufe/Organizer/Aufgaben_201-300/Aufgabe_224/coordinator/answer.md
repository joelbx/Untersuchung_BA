Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py), updated the download and tab progress callers, and moved the color tests alongside the helper. The `colorspace=None` path now validates percentages and preserves the start color’s spec.

Verification: 339 relevant tests passed; `git diff --check` passed. No delegation was used.