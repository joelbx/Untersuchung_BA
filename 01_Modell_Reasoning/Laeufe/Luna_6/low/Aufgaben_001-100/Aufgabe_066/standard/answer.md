Implemented `transformStyleAttributes` to replace inline `height` values containing `vh` with `auto`, preserving other styles. It runs after `transformStylesheet` and before `transformRemote`.

The focused test passed: `yarn workspace proton-mail test --runInBand src/app/helpers/transforms/tests/transformStyleAttributes.test.ts`.