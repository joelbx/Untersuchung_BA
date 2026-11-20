# Checkpoint

Implemented reusable `ExternalLink` in `src/components/views/elements/ExternalLink.tsx`, with native anchor attributes, class composition, `_blank` and `noreferrer noopener` defaults, a decorative CSS mask icon, and a localized screen-reader cue announcing a new tab. Added/imported `res/css/views/elements/_ExternalLink.scss`.

Migrated all settings links that previously opened a new tab to `ExternalLink`, including Profile Settings hosting signup. The room URL in ShareDialog now has localized `title` and `aria-label` text, “Link to room”. Added the English source strings in `src/i18n/strings/en_EN.json`.

Validation: ESLint on all touched TypeScript files with `--max-warnings 0`, Stylelint, and `git diff --check` pass. `yarn lint:types` reports existing errors in thread notification code outside the changes. `yarn test --runInBand` could not run successfully because test setup lacks generated `component-index` and also encounters `localStorage` undefined. No focused tests exist for these components in the checked-out tests.
