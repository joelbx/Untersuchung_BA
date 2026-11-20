# Checkpoint

Task: refactor scanner directory traversal to use fs.FS throughout, remove utils.IsDirReadable, and verify with tests.

State: scanner traversal now takes fs.FS, returns results and error channels, and uses fs.FS for stats, reads, symlink resolution, ignore markers, and readability. Scan constructs os.DirFS at its entry point and restores OS paths for downstream processing. getRootFolderWalker and utils.IsDirReadable were removed.

TDD: added in-memory MapFS test, observed expected API compilation failure before implementation. Added ReadDirFS test, observed `readdir root: invalid argument` failure before implementation; scanner suite passes afterward.

Checks:
- `GOPROXY=off go test ./scanner -count=1`: pass; TagLib C++ deprecation warning emitted.
- `GOPROXY=off go test ./...`: failed in `scanner/metadata/taglib` only. Three failing specs: "correctly parses metadata from all files in folder" (unreadable fixture included because running as root), "Correctly parses m4a (aac) gain tags" (duplicate values), and "correctly handle unreadable file due to insufficient read permission" (root can read fixture). Other packages, including scanner, passed. These failures are outside the refactor and remain unresolved.

Initial environment: `rg` unavailable, so used grep/find. No downloads.
- Repeated `GOPROXY=off go test ./...` after the ReadDirFS change: same three `scanner/metadata/taglib` failures; scanner and all other packages passed.
- Final `GOPROXY=off go test ./scanner -count=1`: pass. `git diff --check`: pass.
