I traced the cleanup failures but did not edit project source or tests because this run is restricted to fault localization.

- [src/groups/cover.js](/app/src/groups/cover.js:64): `Groups.removeCover` clears the three database fields but never deletes the full size cover or thumbnail.
- [src/user/picture.js](/app/src/user/picture.js:204): `User.removeCoverPicture` clears fields only. `removeProfileImage`, `getLocalCoverPath`, and `getLocalAvatarPath` are absent.
- [src/socket.io/user/picture.js](/app/src/socket.io/user/picture.js:47): avatar removal duplicates the field logic and does not await `file.delete`. [src/socket.io/user/profile.js](/app/src/socket.io/user/profile.js:41) needs explicit invalid UID handling and delegation to the user image layer.
- [src/user/delete.js](/app/src/user/delete.js:219): account cleanup searches for fixed filenames, but current uploads use timestamped filenames such as `uid-profileavatar-TIMESTAMP.png`.

The fix needs to validate local upload URL prefixes before mapping them into `upload_path`, remove every associated supported image variant, tolerate missing files, clear the specified fields, and preserve the socket action hooks. The stated filename pattern omits timestamps; the current upload writers include them, so cleanup must account for both. Existing tests assert database changes but do not verify that files were removed.