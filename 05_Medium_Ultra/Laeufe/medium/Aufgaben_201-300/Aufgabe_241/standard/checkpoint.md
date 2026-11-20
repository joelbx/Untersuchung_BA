# Checkpoint

- Goal: make pre-recording Go live and device selection deterministic under repeated interactions.
- Located component and existing tests; repository is clean at start.
- Added a synchronous pending guard and native disabled button for Go live; Promise settlement releases the guard, and synchronous starts hold it for one event tick.
- Added a menu-open guard and non-null device selection callback. The existing audio device hook supplies the updated header label.
- Expanded component tests for repeated initiation, resolution, rejection, synchronous completion, close, and repeated menu activation; updated the button snapshot.
- Focused Jest suite: 11 tests and snapshot pass. ESLint and `git diff --check` pass. Repository-wide TypeScript check reports five unrelated existing MatrixClient typing errors outside changed files.
