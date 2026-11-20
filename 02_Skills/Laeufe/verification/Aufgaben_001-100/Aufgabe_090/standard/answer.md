Updated `/lists/add` input handling so a nonempty POST body is parsed as URL encoded form data and used without query parameters. Defaults no longer mask indexed fields, invalid seed entries are skipped, and later simple-key assignments take precedence during unflattening.

Verification: 18 focused tests passed; Ruff and `git diff --check` passed.