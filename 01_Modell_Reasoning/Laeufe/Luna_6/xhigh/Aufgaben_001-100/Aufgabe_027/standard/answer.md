Updated [lastActivePersistedUserSession.ts](/app/applications/drive/src/app/utils/lastActivePersistedUserSession.ts) to return `number | null`, consider only numeric `ps-` keys, and return `null` when no usable session is found or storage parsing fails. The helper only reads storage.

Updated the public bookmark hook to resume only when it has a local ID; ID `0` remains valid. Updated the existing test expectations.

Verification: the Drive helper test passed (11 tests), and `git diff --check` passed.