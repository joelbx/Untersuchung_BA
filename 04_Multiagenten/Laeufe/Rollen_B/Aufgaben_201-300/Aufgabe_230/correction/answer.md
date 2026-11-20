Fixed both reviewed workflow defects in [affiliate_server.py](/app/scripts/affiliate_server.py): import requests now stage cached products before returning, and repeat requests upgrade a queued identifier’s priority while preserving heap order. Added regression tests for both cases.

Verification: `pytest -q scripts/tests/test_affiliate_server.py` passed (20 tests); `git diff --check` passed.