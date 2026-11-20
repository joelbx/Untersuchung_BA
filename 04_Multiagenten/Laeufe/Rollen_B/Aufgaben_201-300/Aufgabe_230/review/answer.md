VERDICT: FIX

The applied patch has two workflow defects in [affiliate_server.py](/app/scripts/affiliate_server.py):

- Lines 515–521 return a cached product before handling `stage_import=True`. If an earlier request cached the product without staging it, a later import request never queues an import. Stage the cached product or schedule import before returning.
- Lines 528–535 deduplicate a queued identifier without upgrading its priority. A later `high_priority=true` request can remain behind low priority work. Update the queue entry and restore heap ordering.

`pytest -q scripts/tests/test_affiliate_server.py` **passed: 18 tests**. `git diff --check` passed. These passing tests do not cover the two cases above. No project code or tests were changed during this review.