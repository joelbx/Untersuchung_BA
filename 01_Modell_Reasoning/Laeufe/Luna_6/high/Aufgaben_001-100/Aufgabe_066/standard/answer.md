Implemented the inline style transformation and added it to `prepareHtml` after `transformStylesheet` and before `transformRemote`.

The transform changes `height` values containing `vh` to `auto`, while preserving other declarations and `!important`.

Validation: `transformRemote.test.ts` passed (4 tests), and `git diff --check` passed. The mail-wide TypeScript check stopped at Node’s 2 GB heap limit.

Files: [transformStyleAttributes.ts](/app/applications/mail/src/app/helpers/transforms/transformStyleAttributes.ts), [transforms.ts](/app/applications/mail/src/app/helpers/transforms/transforms.ts).