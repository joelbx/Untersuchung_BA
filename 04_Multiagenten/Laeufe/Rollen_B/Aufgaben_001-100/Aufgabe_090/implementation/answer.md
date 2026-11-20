Fixed `/lists/add` input handling. When a form body is present, the list is built from its URL-encoded values without merging query parameters. Defaults no longer conflict with indexed seed fields, invalid seeds are ignored, and later assignments win during unflattening.

The relevant tests pass: **17 passed**. Ruff and `git diff --check` also pass.