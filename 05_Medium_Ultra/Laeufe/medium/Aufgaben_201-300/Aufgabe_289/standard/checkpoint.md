Task: expose canonical config defaults and decode hooks, align Load decoding, preserve schema compatibility.
Implemented: moved existing default fixture into exported DefaultConfig; exported DecodeHooks and used it in Load; added version mapstructure tag; changed Storage Local/Git to pointers with nil-safe validation; updated existing test literals.
Verification: internal/config tests passed; internal/cmd tests still running. git diff --check passed.
