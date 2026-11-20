# Checkpoint

Task: handle unavailable shares in useDefaultShare.
Status: complete.
Changes: exposed isShareAvailable(signal, shareId), using getShare and rejecting locked or soft-deleted metadata; added focused tests for all flag combinations and signal forwarding.
Verification: useDefaultShare.test.tsx passed (7 tests).
