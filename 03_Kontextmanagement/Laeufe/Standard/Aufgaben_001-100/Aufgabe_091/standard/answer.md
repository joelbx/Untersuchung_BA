Implemented `isoneof` and `isnotoneof` for string and number constraints. The evaluator now checks membership in JSON lists, and create and update validation rejects malformed lists, wrong element types, and arrays over 100 items.

The relevant `rpc/flipt` and evaluation package tests pass.