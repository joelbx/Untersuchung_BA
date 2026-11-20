Fixed `/lists/add` form handling. A nonempty POST body is parsed on its own, so query parameters cannot override submitted list fields. Defaults are added after nested fields are reconstructed, malformed or empty seeds are ignored, and the last assignment wins when flattened keys conflict.

The relevant tests passed (17 total), as did `ruff check` and `git diff --check`. No delegation was used.