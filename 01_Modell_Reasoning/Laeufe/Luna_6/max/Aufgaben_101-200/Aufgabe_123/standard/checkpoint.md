# Checkpoint

- Objective: Fix notification HTML rendering and non-success duplicate suppression in `/app`.
- Constraints: Use repository code and existing tests only; do not alter git history, index baseline, or harness configuration.
- Complete: String notification content is sanitized with DOMPurify and rendered as HTML. All rendered links receive `rel="noopener noreferrer"` and `target="_blank"`. Optional keys are accepted and resolved by explicit value, string text, or notification id. Non-success notifications deduplicate by key; success notifications remain distinct.
- Verification: `yarn workspace @proton/components check-types` passed; `yarn workspace @proton/components test` passed (32 suites, 119 passed, 1 skipped); targeted ESLint passed; `git diff --check` passed.
