Added `isoneof` and `isnotoneof` for string and number constraints. Create and update requests now validate JSON array types and enforce the 100-item limit. I added focused tests for matching, invalid values, and the limit boundary.

The `rpc/flipt` and legacy evaluator test suites passed.