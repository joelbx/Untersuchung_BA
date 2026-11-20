# Scanner revert checkpoint

Task: restore native OS directory traversal and add `utils.IsDirReadable`.

Root cause: `TagScanner.Scan` creates `os.DirFS`, and `walkDirTree`, `loadDir`, symlink checks, ignore checks, and readability checks all operate on paths relative to that virtual root. `loadAllAudioFiles` also wraps each OS directory in `os.DirFS`. This keeps the scanner on the fs.FS path that the issue asks to revert. The existing fixture tests cover audio, playlists, symlinks, and ignored folders; `fullReadDir` contains important repeated-error logging behavior.

Hypothesis: passing native absolute paths through `Scan` and `walkDirTree`, then using `os.Stat`, `os.Open`, and `os.ReadDir`, will restore direct traversal while keeping the existing classification and logging behavior. A new utility can centralize the open/close readability check.

Red test: `GOPROXY=off GOSUMDB=off go test ./utils -run '^TestIsDirReadable$' -count=1` fails as expected: `undefined: IsDirReadable`.

Additional root cause found during verification: `walkDirTree` sent traversal errors on an unbuffered channel before closing the results channel, while `Scan` waits for results to close before reading errors. This deadlocked error reporting. `TestWalkDirTreeReportsRootError` reproduced it (`results channel did not close after traversal error`). The error channel now has capacity one.

Implementation: scanner traversal, stat, symlink resolution, ignore markers, and audio directory listing now use OS paths and operations. `utils.IsDirReadable` performs the native open/close check and logs close failures. Windows recycle folders remain ignored. Existing entry read retry/error logs remain in place.

Verification: `GOPROXY=off GOSUMDB=off go test ./scanner ./utils -count=1 -timeout=30s` passed. `git diff --check` passed. The Go build emitted only an existing TagLib deprecation warning.

Status: complete.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find`.
