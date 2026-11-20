Task: Resolve certificate error wrapper constructor and HTML rendering issue.
Status: Complete. WebKit accepts named reply/errors and both positional forms, renders escaped paragraph/list HTML, and handles reply decisions. Shared certificate decision API and Qt5/Qt6 WebEngine wrappers are integrated.
Verification: 12 focused tests passed; 26 WebEngine tab and WebKit network manager tests passed using xvfb-run. git diff --check and compileall passed.
