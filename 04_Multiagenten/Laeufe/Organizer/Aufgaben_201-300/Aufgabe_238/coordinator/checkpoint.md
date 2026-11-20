Task: Replace deprecated :buffer with :tab-select across command registration, completion providers, docs, and examples.
Status: Implemented and verified. No delegation used.
Changes: Renamed command to tab_select, providers to tabs/other_tabs, internal helper to _tabs, updated default gt binding, help docs, test scenarios, manual example. Historical changelog retained as release history.
Tests: completion unit suites 154 passed, 1 xfailed; focused completion assertions 9 passed; WebEngine tab selection scenarios 12 passed, 1 skipped; WebEngine completion scenarios 4 passed. git diff --check clean.
Constraints: local repository/tests only; no git history/index/harness changes.
