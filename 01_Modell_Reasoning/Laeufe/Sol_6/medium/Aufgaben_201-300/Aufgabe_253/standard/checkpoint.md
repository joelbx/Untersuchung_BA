Task: Fix GuiProcess live stderr streaming and per-stream final summaries.
Status: Implemented independent live stdout/stderr updates and ordered final summaries. Updated existing output assertions and added live stream tests. All 42 GuiProcess tests pass; git diff --check passes.
Constraints: Local code/tests only; do not alter git history, index baseline, or harness configuration.
