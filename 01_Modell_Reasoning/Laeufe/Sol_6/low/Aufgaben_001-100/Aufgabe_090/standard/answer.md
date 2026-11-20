Fixed `/lists/add` so a nonempty form body is parsed independently of URL query parameters. Body values now take precedence over defaults without masking indexed `seeds` fields. Invalid or empty reconstructed seeds are ignored, and later assignments to the same simple key win.

Validation: 16 targeted tests passed; Ruff and `git diff --check` passed.