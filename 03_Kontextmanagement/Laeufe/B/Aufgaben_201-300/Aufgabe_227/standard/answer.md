Updated the MIME-suffix workaround to check **runtime Qt only** at the 6.2.3 and 6.7.0 boundaries. I also clarified the `compiled` parameter, made `compiled=True` with `exact=True` raise `RuntimeError`, and added boundary tests.

All **35 relevant tests pass**. A broader run had two unrelated failures under the installed Qt version: a QDataStream status count and a QSaveFile warning.