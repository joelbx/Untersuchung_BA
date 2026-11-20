Notifications now render string HTML through DOMPurify, and links receive `target="_blank"` and `rel="noopener noreferrer"`. Plain strings and React elements remain supported.

Non-success notifications deduplicate by an explicit key, string text, or notification id, in that order. Repeated success notifications remain visible. All 8 focused tests, the component type check, and ESLint passed.