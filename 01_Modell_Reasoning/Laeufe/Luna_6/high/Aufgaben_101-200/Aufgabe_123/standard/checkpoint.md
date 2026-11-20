# Checkpoint

Task: resolve notification HTML rendering and duplicate suppression in `/app`.

Implemented:
- Sanitized string notification content with DOMPurify and forced `target="_blank"` plus `rel="noopener noreferrer"` on resulting links.
- Applied the same link attributes to React-provided anchor elements while preserving React element content.
- Added optional caller-provided notification keys and stable fallback keys (string text or notification id), and deduplicated non-success notifications by key. Success notifications use unique React list keys and are not deduplicated.

Validation:
- `yarn workspace @proton/components check-types` passed.
- `yarn workspace @proton/components lint` passed.
- `yarn prettier --check` on the four changed notification files passed.
- `git diff --check` passed.
- No notification-specific existing test files were found in the components package.
