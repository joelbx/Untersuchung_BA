Updated group and user image removal to delete local cover, thumbnail, and avatar files, including legacy and timestamped variants. Account deletion now cleans both user image types. Socket removal hooks remain in place, and missing files are handled gracefully.

Verification: 340 relevant tests passed; ESLint and `git diff --check` passed.