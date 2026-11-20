Task: Replace deprecated :buffer with :tab-select across command registration, completion, docs, and examples.
Status: complete.
Changes: command dispatcher exposes tab_select with existing count, cross-window, and matching behavior; public completion providers renamed tabs/other_tabs; default gt binding, help, and relevant tests/examples updated. Historical changelog retained.
Verification: completion model suite 73 passed; command and API suite 264 passed, 1 skipped; both pytest processes exited 1 only after an X11 shutdown error following the pass summary. git diff --check passed.
