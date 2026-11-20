Task: refactor walkDirTree to fs.FS and update related helpers/callers; remove IsDirReadable.
Status: implemented and verified.
Changes: walker and helpers use fs.FS; Scan creates os.DirFS at boundary; removed getRootFolderWalker and utils.IsDirReadable; added MapFS traversal test.
Verification: go test ./scanner ./utils passed.
