Fixed inline height handling so `height` values using a `vh` unit become `auto`, while `vh` in comments or quoted text leaves the height unchanged. The transform runs after `transformStylesheet` and before `transformRemote`.

Added regression coverage for the reported `height: 20px /* vh */` case. The reviewer’s exact test command passed: **6 suites, 92 tests**.