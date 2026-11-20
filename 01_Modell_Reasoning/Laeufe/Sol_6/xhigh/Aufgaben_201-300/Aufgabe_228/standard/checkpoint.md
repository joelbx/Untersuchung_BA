# Version parsing issue

Status: complete. Added normalized `QVersionNumber` parser and migrated Qt runtime, distribution, startup, and crash dialog comparisons. Added regression coverage for normalization, minimum versions, and update note. Relevant files: 420 passed, 4 skipped, 1 deselected under `xvfb-run` with exit 0. The existing Chromium initialization test was excluded because it abruptly exits in this environment. `git diff --check` passed.
