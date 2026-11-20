# Checkpoint

Task: add version-aware `auto` mode for `qt.workarounds.disable_accelerated_2d_canvas`.

Plan: inspect Qt argument handling, config schema and tests; migrate the setting to an enum defaulting to `auto`; resolve `auto` from Qt and Chromium versions; run the existing focused Qt args tests.
