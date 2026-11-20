# Checkpoint

Task complete: added `transformStyleAttributes` to replace inline `height` values containing a `vh` unit with `auto`, including the root element. Other declarations and any `!important` priority are preserved. Called it in `prepareHtml` after `transformStylesheet` and before `transformRemote`.

Verification: all 6 mail transform test suites passed (91 tests); `git diff --check` passed.
