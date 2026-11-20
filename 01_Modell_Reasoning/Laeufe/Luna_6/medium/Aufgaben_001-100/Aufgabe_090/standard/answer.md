Updated `/lists/add` input handling so POST form bodies are parsed independently of query parameters, with the first parsed value used per field and defaults applied only when they do not conflict with nested fields. Also updated unflattening so later assignments take precedence and nested values can replace scalar parents.

Relevant existing tests passed: **14 passed**.