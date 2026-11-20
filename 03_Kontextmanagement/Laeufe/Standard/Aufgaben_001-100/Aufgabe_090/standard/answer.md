Updated `/lists/add` so a nonempty POST body is parsed as form data and used without merging query parameters. Indexed seed fields no longer conflict with defaults, invalid seed entries are ignored, and later simple-key assignments win during unflattening.

The relevant tests pass (4 passed). Ruff and `git diff --check` also pass.