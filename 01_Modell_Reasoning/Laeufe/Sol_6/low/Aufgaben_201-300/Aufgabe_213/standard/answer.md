`useDefaultShare` now exposes awaitable `isShareAvailable(signal, shareId)`. It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. The default share loading path remains unchanged.

The Drive test suite passed: **6 tests**, including the new availability and signal-forwarding cases.