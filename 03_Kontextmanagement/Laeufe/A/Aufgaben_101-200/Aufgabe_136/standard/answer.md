Updated the WebKit certificate wrapper to accept `reply` and `errors`, render one error as a paragraph and multiple errors as a list, and HTML-escape every message. Reply actions now occur when a certificate is accepted, not during construction. Added the requested decision state, deferral exception, and Qt5/Qt6 WebEngine wrappers and factory.

Verification: **63 relevant tests passed**.