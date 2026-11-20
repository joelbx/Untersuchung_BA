The scanner now traverses absolute OS paths, uses native filesystem operations for directory and audio file discovery, and checks directory readability through the new [IsDirReadable](/app/utils/paths.go) helper. Ignore rules, symlink handling, and traversal logging remain in place.

Updated the affected scanner tests and added a readability test. `go test ./scanner ./utils` passes.