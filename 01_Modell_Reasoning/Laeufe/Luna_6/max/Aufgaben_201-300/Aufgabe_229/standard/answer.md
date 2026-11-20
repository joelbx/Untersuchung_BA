Implemented uploaded image cleanup.

- Group cover removal now clears all three cover fields and removes matching local cover and thumbnail variants from `upload_path/files` in [cover.js](/app/src/groups/cover.js:66).
- User image removal is centralized in [picture.js](/app/src/user/picture.js:203). It validates local upload paths, removes matching avatar or cover files, and returns the previous avatar fields.
- Account deletion now removes timestamped and legacy cover/avatar files across supported image extensions in [delete.js](/app/src/user/delete.js:220).
- Socket handlers delegate to the user image layer, validate UIDs, and await the existing removal hooks in [user picture handler](/app/src/socket.io/user/picture.js:44) and [user profile handler](/app/src/socket.io/user/profile.js:43).

Verification: `test/user.js` and `test/groups.js` passed, **334 tests**. ESLint, syntax checks, and `git diff --check` passed.