Added a registration token entry view and routed both stable and unstable Matrix auth stages to it. The view accepts Enter or button submission, prevents duplicate submissions while busy, and displays token errors.

The focused Jest suite passes (4 tests), and lint passes. The repository wide TypeScript check still reports existing Sliding Sync errors outside the changed files.