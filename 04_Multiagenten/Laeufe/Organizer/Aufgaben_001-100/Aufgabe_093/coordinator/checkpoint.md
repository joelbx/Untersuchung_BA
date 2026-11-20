Task: Fix Popper placement reporting for RTL layouts in /app.
Status: Complete. Added getInvertedRTLPlacement and rtlPlacement middleware; usePopper returns normalized middleware placement. Exported both utilities and added RTL/LTR tests.
Verification: components Popper Jest suite passed (12 tests); components TypeScript check passed; git diff --check passed.
Delegation: None; solved directly.
