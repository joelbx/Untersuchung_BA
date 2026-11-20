The checked-out patch already handles locked and soft-deleted shares, forwards the abort signal to `getShare`, and preserves the default-share path. The review identified no code defect, so I made no further tracked changes.

The reviewer’s previously interrupted workspace test now passes: **6/6 tests**. `git diff --check` also passes.