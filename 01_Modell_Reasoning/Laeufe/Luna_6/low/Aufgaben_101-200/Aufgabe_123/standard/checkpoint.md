# Checkpoint

Implemented notification content and deduplication changes.

- String notification text is sanitized with the shared DOMPurify helper and rendered as HTML. Sanitized links receive `rel="noopener noreferrer"` and `target="_blank"`.
- Notification creation accepts an optional explicit `key`. Non-success notifications deduplicate by the resolved key (explicit key, string text, or generated notification ID); success notifications always append.
- When a duplicate is replaced, its previous timeout is cleared and the replacement timeout is registered.

Verification: `yarn workspace @proton/components check-types` completed successfully. `yarn workspace @proton/components test --passWithNoTests` passed (32 suites, 119 tests passed, 1 skipped). `git diff --check` passed. There are no tests specifically under `containers/notifications`.
