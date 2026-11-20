Task: Gate MIME suffix workaround using runtime Qt only.
Completed: The workaround calls version_check with compiled=False at both bounds. The version utility documents compiled and raises RuntimeError for compiled=True with exact=True. Added runtime boundary and mismatch tests.
Verification: 17 version_check tests passed; 11 suffix workaround tests passed with QT_QPA_PLATFORM=offscreen. A prior combined run aborted in Qt application fixture setup.
