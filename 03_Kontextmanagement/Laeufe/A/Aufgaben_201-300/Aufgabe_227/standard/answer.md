Updated the MIME suffix workaround to check only runtime Qt for the 6.2.3 inclusive and 6.7.0 exclusive bounds. Clarified `version_check`’s `compiled` parameter and made `compiled=True` with `exact=True` raise `RuntimeError`.

The relevant tests passed: **35 passed** with `QT_QPA_PLATFORM=offscreen`.