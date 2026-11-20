Implemented image cleanup for group covers, user covers and avatars, and account deletion.

- [Group cover removal](/app/src/groups/cover.js) deletes local cover and thumbnail files under `upload_path/files` and clears all cover fields.
- [User image handling](/app/src/user/picture.js) adds validated local path getters and centralized removal functions that clear the related fields.
- [Socket handlers](/app/src/socket.io/user/picture.js) and [profile handlers](/app/src/socket.io/user/profile.js) use the centralized cleanup and retain plugin action hooks.
- [Account deletion](/app/src/user/delete.js) removes timestamped and legacy cover/avatar files in PNG, JPEG, JPG and BMP formats.

ESLint and `git diff --check` pass. The existing removal tests could not run because the test harness could not connect to Redis at `127.0.0.1:6379`. The checkpoint is recorded in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).