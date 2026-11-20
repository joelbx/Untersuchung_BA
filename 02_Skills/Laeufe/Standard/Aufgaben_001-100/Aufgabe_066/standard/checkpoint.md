# Checkpoint

Task: Replace inline `height` values containing `vh` with `auto` in mail HTML, after `transformStylesheet` and before `transformRemote`.

Status: implemented and verified. `rg` was unavailable, so local `grep` and `find` were used.

Changes:
- Added `transformStyleAttributes` to set inline `height` values containing `vh` to `auto`, including on the root element and preserving `!important`.
- Called it between `transformStylesheet` and `transformRemote` in `prepareHtml`.
- Added a focused test for root and descendant styles, other declarations, and `!important`.

Checks:
- `cd applications/mail && ../../node_modules/.bin/jest src/app/helpers/transforms/tests --runInBand --coverage=false --silent`: 6 suites, 90 tests passed.
- Prettier check and ESLint on changed TypeScript files: passed.
- `git diff --check`: passed.
- Initial Jest invocation from `/app` used the wrong config and failed to parse TypeScript; rerunning from `applications/mail` passed.
