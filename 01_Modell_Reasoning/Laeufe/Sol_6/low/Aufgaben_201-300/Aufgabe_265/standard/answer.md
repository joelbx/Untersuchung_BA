Updated `QtColor` so HSV and HSVA hue percentages scale to 359, while saturation, value, alpha, and RGB percentages scale to 255. The parser now validates the function name and component count before constructing a `QColor`.

All 31 focused `QtColor` tests pass. The full config type test file encountered unrelated Hypothesis fixture health check failures, so it did not complete.