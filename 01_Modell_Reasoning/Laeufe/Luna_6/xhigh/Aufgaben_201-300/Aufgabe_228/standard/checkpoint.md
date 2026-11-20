# Checkpoint

Completed the Qt-native version parsing migration.

- Added normalized `utils.parse_version()` returning `QVersionNumber`.
- Updated Qt runtime checks to use `QLibraryInfo.version()` and Qt comparisons; migrated early initialization, distribution metadata, and crash dialog version notes.
- Updated existing version-related test fixtures to use the new Qt-native API.
- Verification: 318 relevant utility/early-init/crash-dialog tests passed; 19 distribution and sandbox tests passed.
