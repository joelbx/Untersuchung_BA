Fixed the QtWebEngine file picker so accepted image MIME types include missing filename extensions on affected Qt versions (6.2.3 through 6.6.x). `chooseFiles` now passes those extensions to Qt’s picker without duplicating extensions already accepted.

The focused webview tests pass: **11 passed**.