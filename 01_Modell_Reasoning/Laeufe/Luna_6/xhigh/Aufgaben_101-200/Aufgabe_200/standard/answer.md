Implemented `utils.parse_duration` for decimal h/m/s components, inter-unit whitespace, and bare integer milliseconds. Updated `:later` to use it and report invalid durations as command errors.

Validation: 164 existing tests passed; `git diff --check` was clean. Work recorded in [checkpoint.md](/app/.codex-role-output/checkpoint.md).