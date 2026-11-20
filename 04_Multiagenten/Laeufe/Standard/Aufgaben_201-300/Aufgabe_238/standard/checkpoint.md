Task: replace deprecated :buffer with :tab-select in command registration, completion providers, help, default configuration, and active examples/tests.
Status: complete.
Changes: renamed CommandDispatcher.buffer to tab_select; renamed miscmodels.buffer/other_buffer to tabs/other_tabs; updated all active :buffer references outside historical changelog; added count-precedence end-to-end scenario.
Verification: 136 unit tests passed; 14 focused QtWebEngine end-to-end scenarios passed, 1 existing skipped; direct command/provider registration assertions passed; git diff --check passed; no active :buffer references under qutebrowser, doc/help, or tests.
