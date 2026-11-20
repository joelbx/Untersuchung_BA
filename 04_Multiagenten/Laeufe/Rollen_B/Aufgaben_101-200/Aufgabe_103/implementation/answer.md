Updated the RPM parsers to preserve empty release fields, format source package versions without a trailing hyphen, and parse the requested `-src.rpm` filenames. Malformed filenames now return an error. The update parser also treats a `(none)` epoch as absent.

Focused scanner tests pass, including the new empty-release and filename cases. `git diff --check` passes.