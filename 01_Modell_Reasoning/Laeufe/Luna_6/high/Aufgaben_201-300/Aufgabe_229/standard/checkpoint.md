# Checkpoint

Task: remove orphaned uploaded group covers and user cover/avatar files during explicit removal and account deletion.

Implemented:
- Group cover removal resolves only URLs in the uploads `files` URL prefix into `upload_path/files`, deletes cover and thumbnail files, then clears all three cover fields.
- User image helpers validate upload URL prefixes and UID-specific image names, find existing cover/avatar paths across png/jpeg/jpg/bmp variants, and centralize removal and field clearing.
- Avatar and cover socket handlers delegate to the image layer and retain their plugin action hooks; cover removal rejects invalid UIDs.
- Account deletion invokes centralized cleanup and removes timestamped and non-timestamped image variants.

Verification:
- ESLint passed for all edited JavaScript files.
- `git diff --check` passed.
- Existing `test/user.js` and `test/groups.js` were attempted, but their setup failed because Redis is unavailable at `127.0.0.1:6379` (0 tests ran).
