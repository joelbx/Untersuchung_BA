# Checkpoint

Task: Move MIME suffix workaround into a pure module-level helper and update WebEnginePage.chooseFiles to pass merged suffixes through the superclass.

Completed: Added module-level `extra_suffixes_workaround`, including early Qt version gating, exact MIME matching, wildcard expansion via `mimetypes.types_map`, and exclusion of already supplied suffixes. Updated `chooseFiles` to merge and deduplicate the original values with helper output, with exactly one superclass call site and no per-instance data use. Preserved external file-picker handling. Updated existing tests for the module-level helper and `None` receiver.

Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` passed (20 tests). `git diff --check` passed. The initial pytest invocation without offscreen platform aborted during Qt application fixture startup; the offscreen rerun passed.
