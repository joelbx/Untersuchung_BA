VERDICT: FIX

[transformStyleAttributes.ts](/app/applications/mail/src/app/helpers/transforms/transformStyleAttributes.ts:4) matches `vh` anywhere in a height declaration, including comments. I reproduced `height: 20px /* vh */` changing from a valid `20px` height to `auto`. Match the `vh` unit in the CSS value while excluding comments, and preserve heights that do not use that unit.

The call in [transforms.ts](/app/applications/mail/src/app/helpers/transforms/transforms.ts:55) is in the required order. `yarn workspace proton-mail test src/app/helpers/transforms/tests --runInBand --watch=false` passed: 6 suites, 91 tests. No TEST_ENVIRONMENT_PROBLEM. I made no project code or test changes as the independent reviewer.