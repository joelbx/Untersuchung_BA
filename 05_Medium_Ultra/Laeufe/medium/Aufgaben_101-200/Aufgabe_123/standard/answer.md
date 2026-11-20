Fixed notifications in `/app`. String content now renders as sanitized HTML, and links receive `target="_blank"` and `rel="noopener noreferrer"`. Non-success notifications deduplicate by an explicit key, then string text, then notification ID; repeated success notifications remain visible.

The focused tests pass (10/10), as do the components TypeScript and formatting checks.