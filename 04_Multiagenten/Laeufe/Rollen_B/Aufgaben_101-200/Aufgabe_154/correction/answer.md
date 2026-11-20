Fixed CLIXML replacement so adjacent `<Objs>` elements are parsed independently. A malformed element now stays unchanged without preventing a valid neighbor from being decoded. Added a regression test for that case.

The reviewer’s test command passed: **47 passed**. `git diff --check` passed. No test environment problems remain.