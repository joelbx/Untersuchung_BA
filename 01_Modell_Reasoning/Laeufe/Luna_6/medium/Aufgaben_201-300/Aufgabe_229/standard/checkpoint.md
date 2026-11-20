# Checkpoint

Task: fix local disk cleanup for group covers and user cover/avatar images on explicit removal and account deletion.

Implemented:
- Group cover removal deletes local full-size and thumbnail files only when their URLs use the configured uploads/files URL prefix, then clears all three cover fields.
- User image logic now resolves local cover/avatar files, validates profile upload URLs before unlinking, centralizes uploaded avatar and cover removal, and clears the associated database fields.
- Socket handlers delegate to the centralized removal functions and continue firing their action hooks; cover removal validates the target uid.
- Account deletion scans the profile upload directory for all supported cover/avatar extensions, including timestamped uploads.

Validation:
- ESLint passed for all changed JavaScript files.
- `git diff --check` passed.
- `npx mocha test/user.js` could not run because Redis at 127.0.0.1:6379 refused the connection during the suite setup hook (0 tests executed).
