Task: replace deprecated :buffer with :tab-select throughout command registration, completion, documentation, and examples.
Status: complete. Renamed command and completion providers; updated default binding, generated help, and existing tab/completion scenarios. Added count precedence scenario.
Verification: focused unit suite 294 passed, 1 skipped; selected WebEngine end-to-end scenarios 14 passed, 1 skipped; generated command and settings help match checked-in files; git diff --check clean.
Constraints: used local repository and existing tests only; preserved git history/index and harness configuration.
