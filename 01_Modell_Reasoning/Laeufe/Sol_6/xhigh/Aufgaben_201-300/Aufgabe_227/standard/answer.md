Updated the MIME-suffix workaround to check **runtime Qt only** at both bounds: ≥ 6.2.3 and < 6.7.0. Clarified `version_check`’s `compiled` parameter and made `compiled=True, exact=True` raise `RuntimeError`. Added tests for mismatched runtime and compiled versions.

The 34 targeted tests pass. The full affected modules had 196 passes and two unrelated Qt 6.9 test failures.