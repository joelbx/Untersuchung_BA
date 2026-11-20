# Checkpoint

Task: add `scrolling.bar = overlay`, enable Chromium OverlayScrollbar only for QtWebEngine on non-macOS Qt 5.11+, update boolean migration, and keep relevant flag/header tests working.

Completed: accepted and documented `overlay`; emit `--enable-features=OverlayScrollbar` only for QtWebEngine on non-macOS Qt 5.11+; migrate `False` to `overlay`; register and apply `@js_headers` for the QtWebEngine 5.12 through 5.14 dynamic-header bug; mark the two JS header scenarios. Added tests for the flag matrix, stylesheet fallback, flag order independence, migration, and marker behavior.

Verification: 386 passed, 1 skipped, 1 rerun (exit 0) across the relevant config, browser shared, and marker tests using Qt offscreen and disabled WebEngine sandbox in this root container. BDD collection selected exactly the two JS header scenarios with `-m js_headers`. `git diff --check` passed.
