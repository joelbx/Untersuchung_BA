Updated the RPM parsers to preserve empty release fields, omit the trailing hyphen from source package versions, parse `-src.rpm` filenames, and reject malformed filenames. Update candidate parsing now treats `(none)` as an absent epoch. Added regression tests.

The focused scanner tests and `git diff --check` passed.