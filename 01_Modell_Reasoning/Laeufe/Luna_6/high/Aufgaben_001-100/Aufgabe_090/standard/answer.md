Fixed `/lists/add` so nonempty POST bodies are parsed independently of query parameters, body values override defaults, and nested fields are not masked by parent defaults. Seed parsing now skips invalid or empty entries, and unflattening allows later assignments to take precedence.

Validation passed: 14 existing list and utility tests, plus `git diff --check`.