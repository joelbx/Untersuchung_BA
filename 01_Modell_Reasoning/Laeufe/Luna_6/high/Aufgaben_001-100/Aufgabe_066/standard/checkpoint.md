# Checkpoint

Implemented `transformStyleAttributes` in `applications/mail/src/app/helpers/transforms/transformStyleAttributes.ts`. It checks the root and every descendant with a `style` attribute, changes inline `height` values containing `vh` to `auto`, and retains other declarations and the `!important` priority.

Integrated the transform in `prepareHtml` immediately after `transformStylesheet` and before `transformRemote`.

Validation: Existing `transformRemote.test.ts` passed (4 tests). `yarn workspace proton-mail check-types --pretty false` could not complete because Node reached its default 2 GB heap limit. `git diff --check` passed.
