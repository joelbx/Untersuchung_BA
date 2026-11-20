Added `transformStyleAttributes` to replace inline `height` values containing `vh` with `auto`, including on the root element. It preserves other styles and `!important`, and runs after `transformStylesheet` and before `transformRemote`.

Verification passed: all 90 transform tests, Prettier, ESLint, and `git diff --check`.