Refactored directory traversal to use `fs.FS` throughout, moved walker startup into `Scan`, and removed `utils.IsDirReadable`. Added an in-memory filesystem test for traversal and ignore markers.

`go test ./scanner ./utils` passed with downloads disabled.