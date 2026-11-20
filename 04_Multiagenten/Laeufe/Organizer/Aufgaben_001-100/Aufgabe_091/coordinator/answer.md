Added `isoneof` and `isnotoneof` for string and number constraints. Evaluation now checks membership in JSON arrays; create and update validation rejects invalid types, malformed arrays, and lists over 100 items.

The evaluator and `rpc/flipt` tests pass. I completed the work directly; there were no delegations or adoption decisions.