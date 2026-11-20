Correction round complete. The existing helper returns dot-prefixed input entries on affected runtime Qt versions. chooseFiles now deduplicates its filter list while retaining input order; the existing .jpg case verifies no duplicate is passed. Updated the test expectation accordingly.

Reviewer test commands rerun:
- Focused version_check/suffixes_workaround command: 31 passed, 164 deselected.
- Full qtutils/webview command: 193 passed, 2 failed, 6 rerun.

TEST_ENVIRONMENT_PROBLEM: Runtime Qt 6.9.1 adds a fifth QDataStream.Status value and emits a QSaveFile::commit warning in two unrelated existing tests. Their failures match the review report. git diff --check passed.
