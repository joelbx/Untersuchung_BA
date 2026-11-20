# Checkpoint

- Task: replace inline `height` values using viewport-height units with `auto` in mail HTML, after stylesheet transformation and before remote transformation.
- Status: implemented and verified.
- Added `transformStyleAttributes` to replace inline `height` values using `vh` with `auto`, including the root element. The helper preserves other raw style declarations, including remote image placeholders.
- Invoked the helper after `transformStylesheet` and before `transformRemote` in `prepareHtml`.
- Verification: 3 relevant Jest suites passed (43 tests); targeted ESLint and Prettier checks passed; `git diff --check` passed.
