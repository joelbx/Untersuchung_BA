Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py) and updated the download and tab progress indicators to call the new location. Added regression coverage for progress colors, invalid percentages, and color space behavior.

Verification: **344 relevant tests passed**.