# Checkpoint

Issue: Replace inline CSS `height` values containing `vh` with `auto` during HTML preparation, after `transformStylesheet` and before `transformRemote`.

Implementation: Added `transformStyleAttributes` to inspect the supplied root element and every descendant with a `style` attribute. It updates only the parsed `height` declaration, preserves its priority and all unrelated declarations, and runs at the required point in `prepareHtml`.

Validation: All five existing HTML transform suites passed (89 tests). `git diff --check` passed.
