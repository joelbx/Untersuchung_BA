Added `qcolor_to_qsscolor` to convert `QColor` values to `rgba(r, g, b, a)` strings, including the default alpha value. The WebView and TabBar background stylesheet templates now use it.

All 123 `qtutils` tests pass. The TabWidget suite stops during setup because its existing icon-size code passes a float to `QSize`; it does not reach the changed color code.