Progress: Fault localization complete. No project source or tests modified.
Findings:
- src/groups/cover.js removeCover deletes DB fields only. Full and thumbnail URLs are separate local uploads under files; resolve only validated local URL prefixes to upload_path/files.
- src/user/picture.js removeCoverPicture deletes DB fields only; removeProfileImage and getLocalCoverPath/getLocalAvatarPath are absent. Existing deleteCurrentPicture handles replacement only, checks hard-coded /assets/uploads/profile/, and removes just the referenced filename.
- src/socket.io/user/picture.js removeUploadedPicture builds a base_dir/public path, does not await file.delete, and duplicates DB cleanup. src/socket.io/user/profile.js passes a data object to removeCoverPicture and has no explicit invalid-data guard for null/invalid uid.
- src/user/delete.js deleteImages searches fixed uid-profilecover.ext and uid-profileavatar.ext names, while current uploads use uid-profilecover-TIMESTAMP.ext and uid-profileavatar-TIMESTAMP.ext. Its allowed extension list can vary with plugins.
- Existing tests in test/user.js and test/groups.js assert field removal only; no disk-removal assertions found. Group getGroupFields and user getUserFields can transform stored URLs with relative_path/defaults, so raw DB URL fields are preferable for safe path validation.
Uncertainty: Interface filename pattern omits timestamps, unlike current writers. Cleanup should cover both legacy fixed names and current timestamped names if all associated images must be removed.
