# Checkpoint

Task: Fix cleanup of locally uploaded user/group cover and avatar images on explicit removal and user account deletion.

Implementation: Group cover removal now reads the stored cover and thumbnail URLs, accepts only the configured relative uploads route, maps filenames into `upload_path/files`, deletes local files, and clears all three cover fields. User image cleanup is centralized in `src/user/picture.js`; local path getters validate the upload URL, user id, filename pattern, extension, target directory, and file existence. Avatar/cover socket handlers invoke those utilities and retain their plugin action hooks. Account deletion sweeps timestamped and legacy cover/avatar filenames for the user across PNG, JPEG, JPG, and BMP.

Verification: Changed JavaScript files pass ESLint, `git diff --check` passes, and the final working-tree review shows only the intended source edits. The relevant existing Mocha tests were attempted with `npm test -- --grep 'remove cover|remove uploaded picture'`, but the suite's global setup could not connect to Redis at `127.0.0.1:6379` (`ECONNREFUSED`), so no tests ran.
