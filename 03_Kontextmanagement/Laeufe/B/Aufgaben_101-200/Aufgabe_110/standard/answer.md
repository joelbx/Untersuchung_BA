Implemented the mechanism-segmented download counter, its schema, and size propagation through stateful and preview flows. The file saver and metrics hook now use the same mechanism selector.

Verification passed: 20 focused tests, Drive and metrics type checks, formatting, and `git diff --check`. This work item is complete.