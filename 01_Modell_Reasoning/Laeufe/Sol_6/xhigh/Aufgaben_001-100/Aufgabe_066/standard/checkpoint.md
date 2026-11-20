# Checkpoint

- Task: replace inline `height` values containing `vh` with `auto` during mail HTML preparation.
- Located the preparation pipeline in `applications/mail/src/app/helpers/transforms/transforms.ts`.
- Added `transformStyleAttributes` to replace inline `height` values with a `vh` unit, including on the root element, while retaining other declarations and height priority.
- Invoked it in `prepareHtml` after `transformStylesheet` and before `transformRemote`.
- Added focused tests. Six transform suites passed (91 tests); ESLint, Prettier, and `git diff --check` passed.
