Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py) and updated the download and tab progress indicators to use the new location. Interpolation now rejects percentages outside 0–100 even when the colorspace is `None`.

The relevant utility, download, and tabbed browser tests passed: **335 passed**.