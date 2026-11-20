Added `qcolor_to_qsscolor` to convert named, RGB, and RGBA `QColor` values into QSS strings, including the alpha channel. `WebView` and `TabBar` now use it in their background stylesheet templates. Added conversion tests; all 123 utility tests pass.

The TabWidget suite stops during setup because its existing icon-size code passes a float to `QSize`, before it reaches the changed color setter.