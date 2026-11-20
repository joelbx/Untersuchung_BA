Implemented Qt-native version parsing with `utils.parse_version` and updated the requested Qt, early initialization, distribution, and crash dialog checks.

The focused test run reached 100% across 416 tests, with expected skips and reruns. `git diff --check` passed. I also updated distribution test expectations to use `QVersionNumber`.