Fixed `/lists/add` input handling. When a form body is present, the server parses its first value per field and builds the list without merging query parameters. Indexed seeds now ignore invalid or empty entries, and `unflatten()` lets later simple-key assignments win.

The relevant existing tests pass: **17 passed**.