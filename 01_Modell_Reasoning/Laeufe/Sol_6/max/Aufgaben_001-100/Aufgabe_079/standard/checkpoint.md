# Checkpoint

Issue: Restore scanner traversal through OS filesystem paths and add utils.IsDirReadable.

Initial findings: `scanner/walk_dir_tree.go` and `scanner/tag_scanner.go` currently pass `fs.FS` and relative paths. Scanner tests cover traversal and entry handling; Windows-specific tests also exist. No user changes were present in `git status --short` at start.

Plan: Convert scanner APIs to absolute/native paths, preserve traversal logging and ignore rules, add OS readability helper, update existing scanner tests, and run relevant local tests without downloads.

Completed: Scanner traversal, empty-folder detection, symlink/ignore checks, and audio listing now use OS filesystem operations. Walker reports absolute paths and buffers traversal errors so callers can drain results before reading errors. Added utils.IsDirReadable with close-error logging. Updated scanner and Windows-specific tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./scanner ./utils` passed; `git diff --check` passed. Existing TagLib C++ deprecation warning appeared during test compilation.
