Task: Handle unavailable locked or soft-deleted shares in useDefaultShare.
Progress: Added isShareAvailable to useDefaultShare and availability cases to its existing test file.
Validation: yarn workspace proton-drive test useDefaultShare.test.tsx passed (6 tests).
