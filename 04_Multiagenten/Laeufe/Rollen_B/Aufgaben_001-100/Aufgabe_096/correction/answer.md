Updated `atomic_move()` to restrict a new file’s source before rename and to create files through the unsafe write path with restrictive permissions. The existing default permission and warning behavior remains in place. I also isolated shared warning state in the tests.

The reviewer’s flagged test commands now pass, including the combined run: **51 passed**. `git diff --check` is clean.