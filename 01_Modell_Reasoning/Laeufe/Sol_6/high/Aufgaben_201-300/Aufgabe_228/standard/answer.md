Added [utils.parse_version](/app/qutebrowser/utils/utils.py) to return a normalized `QVersionNumber` and updated the Qt, distribution, and crash-dialog checks to use Qt-native version comparisons.

Tests: **421 passed, 4 skipped** across the affected modules with one unrelated Chromium initialization test excluded. The unfiltered run exits during that test without a pytest failure summary.