Implemented `transformStyleAttributes` to change inline `height` values containing a `vh` unit to `auto`, preserving other declarations and `!important`. It runs after `transformStylesheet` and before `transformRemote`.

Changed [transformStyleAttributes.ts](/app/applications/mail/src/app/helpers/transforms/transformStyleAttributes.ts) and [transforms.ts](/app/applications/mail/src/app/helpers/transforms/transforms.ts).

Validation: all five existing transform suites passed (89 tests), and `git diff --check` passed.