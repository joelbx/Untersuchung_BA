# Checkpoint

Task: replace inline height values containing `vh` with `auto` in mail HTML and call the transform after `transformStylesheet` and before `transformRemote`.
Status: implemented and verified.
Files: new `transformStyleAttributes.ts`, its focused test, and pipeline call in `transforms.ts`.
Verification: transform test suite passed (6 suites, 91 tests); Prettier check and git diff --check passed.
Delegation: none.
