Task: add non-destructive preview to import pipeline and HTTP endpoints, with observable author/language/cover validation.
Status: implemented in checked-out files. Preview returns simulated UUID keys, edits, and cover acceptance; skips writes, cover upload, and Archive.org updates. Added tests for new and matched preview paths and cover host validation.
Verification: 131 relevant tests passed; ruff check and git diff --check passed.
