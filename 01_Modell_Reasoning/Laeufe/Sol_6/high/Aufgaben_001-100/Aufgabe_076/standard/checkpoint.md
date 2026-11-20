# Checkpoint

- Task: normalize address tokens split on commas and semicolons, and form recipients with identical bare email names and addresses.
- Initial working tree: clean.
- Implemented `splitBySeparator` in the shared recipient module and used it in both autocomplete components.
- `inputToRecipient` now uses the bare address for both `Name` and `Address`.
- Added shared parsing tests. Focused Karma run: 4 passed. Shared and components type checks passed. Prettier check passed.
- Full shared Karma run: 837 passed, 2 unrelated failures in cookie expiration and empty-file base64 tests under system Chromium.
