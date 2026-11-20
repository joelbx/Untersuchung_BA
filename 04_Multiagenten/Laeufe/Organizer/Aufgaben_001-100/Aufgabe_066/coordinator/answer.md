Added `transformStyleAttributes` to change inline `height` values containing `vh` to `auto`, including on the root element. It preserves other styles and `!important`. The mail HTML pipeline now calls it after `transformStylesheet` and before `transformRemote`.

Verification: all 91 transform tests passed across 6 suites; formatting and `git diff --check` passed. No delegation was used.