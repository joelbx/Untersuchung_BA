Fixed `/lists/add` so POST form values take precedence without merging query parameters. Indexed seeds are reconstructed before defaults are applied, invalid seed entries are ignored, and later unflatten assignments win.

The focused tests pass (5/5); Ruff and `git diff --check` pass.