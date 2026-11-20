Task: Add QColor to QSS RGBA conversion utility and use it for WebView and TabBar background styles.
Status: complete.
Changes: qcolor_to_qsscolor added in qtutils; WebView and TabBar QSS templates use it while retaining palette updates; unit coverage includes named colors, RGB, RGBA.
Verification: 123 qtutils tests passed; compileall and git diff --check passed. TabWidget suite could not complete because existing _set_icon_size passes a float to QSize before changed color code runs (PyQt 5.15.9).
