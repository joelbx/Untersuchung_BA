Fixed the share lookup issue in both copies of the invitations store, members store, and member view. Missing share IDs such as `toString` now return empty arrays, while stored data remains isolated by share.

The flagged store test passes (3 tests), both workspace type checks pass, and `git diff --check` passes.