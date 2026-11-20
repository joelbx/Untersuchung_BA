# Image cleanup issue checkpoint

- Task: remove orphaned local group covers and user cover/avatar files during explicit removal and account deletion.
- Repository state at start: clean working tree.
- Found: group removal only deleted database fields; socket avatar deletion used an incorrect disk path; account deletion missed timestamped files.
- Implemented: URL scoped group file deletion, user image cleanup for legacy and timestamped names, socket delegation, and account deletion through the user image layer.
- Regression coverage: group cover/thumbnail cleanup across extensions, user cover/avatar cleanup, plugin hooks, unsafe paths, missing files, and account deletion.
- Verification: combined `test/imageCleanup.js`, `test/user.js`, and `test/groups.js` run passed (339 tests); focused regression rerun passed (5 tests); ESLint and `git diff --check` passed.
- Final state: changes remain in checked-out files for coordinator export; no git history or index changes.
