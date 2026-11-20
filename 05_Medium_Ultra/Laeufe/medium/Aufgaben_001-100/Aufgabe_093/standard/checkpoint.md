Task: Fix RTL placement reporting in Popper.
Status: Complete.
Changes: Added getInvertedRTLPlacement and rtlPlacement middleware; usePopper exposes normalized placement; exported helpers; added focused utility and middleware tests.
Verification: Popper utils Jest suite passes (7 tests); components TypeScript check passes; Prettier check and git diff --check pass.
