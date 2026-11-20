Fixed the duplicate file filters: `chooseFiles` now preserves filter order while passing each entry only once. The `.jpg` test expectation now checks that behavior.

The reviewer’s focused command passed (31 tests). The full command passed 193 tests and still has two unrelated **TEST_ENVIRONMENT_PROBLEM** failures under Qt 6.9.1: the `QDataStream.Status` count and a `QSaveFile::commit` warning.