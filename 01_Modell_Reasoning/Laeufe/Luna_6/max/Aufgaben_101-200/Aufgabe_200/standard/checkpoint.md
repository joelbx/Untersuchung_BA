# Checkpoint

- Task: add unit-aware duration parsing for `:later` while preserving numeric millisecond input.
- Implemented `utils.parse_duration` for ordered `h`/`m`/`s` components, decimal values, whitespace between components, and digit-only millisecond values; invalid or empty input raises `ValueError`.
- Updated `:later` to accept a string duration, use `parse_duration`, and convert parsing errors to `CommandError`.
- Existing targeted tests: 164 passed. Pytest returned exit code 1 during X11 teardown (`XIO: fatal IO error`), including with Qt offscreen mode.
- Final `git diff --check` passed.
