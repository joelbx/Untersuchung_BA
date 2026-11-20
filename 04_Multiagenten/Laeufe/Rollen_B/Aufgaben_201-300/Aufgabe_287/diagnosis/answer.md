I localized the missing image paths, but did not edit project source or tests: the task constraints for this run require a diagnosis only.

- [scanner/walk_dir_tree.go](/app/scanner/walk_dir_tree.go:65) records `HasImages` but discards image names. `dirStats` needs a list populated for every detected image.
- [model/mediafile.go](/app/model/mediafile.go:72) lacks `MediaFiles.Dirs()`. It should return sorted, unique parent directories from media file paths. [model/album.go](/app/model/album.go:5) lacks the album `ImageFiles` field.
- [scanner/tag_scanner.go](/app/scanner/tag_scanner.go:98) refreshes changed folders before the filesystem directory map is complete. The complete map must reach changed and deleted directory handlers and the refresher; `folderHasChanged` can lose its unused context argument.
- [scanner/refresher.go](/app/scanner/refresher.go:68) persists each album immediately after `ToAlbum()`. Before `Put`, it should join each album directory with that directory’s image names, then join the full paths with `filepath.ListSeparator`.
- A new migration under [db/migration](/app/db/migration) must add `album.image_files` and call the existing `forceFullRescan` helper.

Existing tests cover adjacent scan and album behavior, but none verify multiple images across album directories or removal during an incremental rescan. Whether any client endpoint needs an additional mapping beyond the album model’s JSON field remains unverified.