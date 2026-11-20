# Checkpoint

Issue: add `scrolling.bar=overlay` with platform and Qt gating, migrate legacy booleans, and support `js_headers` test gating.

Changes in progress: added the configuration value and documentation, migrated legacy `False` to `overlay`, and gated the Chromium flag on QtWebEngine, Qt runtime 5.11+, and non-macOS. Added argument, CSS fallback, migration, and marker tests. `@js_headers` now follows the existing Qt 5.12–5.14 dynamic-header workaround.

Verification complete: 337 focused tests passed, 1 skipped, 1 unrelated dark-mode Chromium probe deselected because it segfaults in this headless QtWebEngine setup. Both `@js_headers` scenarios collect with the marker; the scenario with `@qtwebkit_skip` retains both tags. The full QtWebEngine end-to-end run cannot start because the offscreen subprocess cannot create an OpenGL context. `git diff --check` passes.
