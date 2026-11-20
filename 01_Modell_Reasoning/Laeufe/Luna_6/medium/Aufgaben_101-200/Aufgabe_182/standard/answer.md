Implemented forked display routing through `_final_q`. The proxy preserves the method name and forwards only caller-supplied arguments; the results thread invokes the matching `Display` method.

Updated the fork display test to expect the new call format. Focused tests pass: **10 passed, 1 skipped**. `git diff --check` is clean.