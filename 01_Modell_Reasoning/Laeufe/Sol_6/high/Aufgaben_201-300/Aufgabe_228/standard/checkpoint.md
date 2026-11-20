Task: Replace specified non-Qt version parsing with a shared QVersionNumber parser.
Status: Implemented and verified. All affected test modules pass with the unrelated QtWebEngine initialization test excluded: 421 passed, 4 skipped, 1 deselected. The full run exits during TestChromiumVersion.test_unpatched without a pytest summary in this environment.
Final checks: git diff --check passed; no history, index, or harness changes.
