# Checkpoint

Issue: Convert inline `height` declarations containing the `vh` unit to `auto` when preparing HTML email content, after `transformStylesheet` and before `transformRemote`.

Implementation:
- Added `transformStyleAttributes(document: Element)` to inspect a styled root element and every styled descendant, changing only `height` when its inline value contains `vh` (case-insensitive).
- Integrated the helper in `prepareHtml` between `transformStylesheet` and `transformRemote`.

Verification:
- Existing transform test folder: 5 suites and 89 tests passed.
- Targeted ESLint check: passed.
- Prettier check: passed.
- App-wide TypeScript check did not complete: Node reached its default heap limit (about 2 GB).
