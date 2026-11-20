VERDICT: FIX
Reviewed current diff in scripts/affiliate_server.py and scripts/tests/test_affiliate_server.py. Relevant test command `pytest -q scripts/tests/test_affiliate_server.py` succeeded: 18 passed in 0.76s. `git diff --check` succeeded with no output.
Code defects:
1. scripts/affiliate_server.py:515-521 returns any cached product immediately, so a product cached from stage_import=false is never staged when a later stage_import=true request arrives. Route the staging request through import scheduling (or stage directly from cached metadata) before returning.
2. scripts/affiliate_server.py:528-535 deduplicates an already queued identifier without upgrading priority. A later high_priority=true request remains LOW and can miss its retry window. Reinsert/update the queue item safely with HIGH priority when needed.
No project code or tests changed during review.
