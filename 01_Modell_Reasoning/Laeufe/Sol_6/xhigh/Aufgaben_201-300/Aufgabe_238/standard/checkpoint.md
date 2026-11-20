Task: Replace deprecated :buffer with :tab-select across command registration, completion, help, examples, and tests.
Status: Complete. :tab-select is the registered command; tabs/other_tabs are the completion providers. Default gt binding, help pages, scenarios, and manual example updated.
Verification: 73 completion model unit tests passed; 31 config data unit tests passed; 15 focused end-to-end scenarios passed and 1 existing flaky scenario skipped. Command registry excludes buffer; generated command and settings help match checked-in docs; git diff --check passes.
Constraints observed: local code/tests only; git history, index, and harness configuration unchanged.
