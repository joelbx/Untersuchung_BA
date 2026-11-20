Resolved the validation gap. `flipt validate` now reports unknown rule variants and segments as individually unwrap-able errors with file, line, and column locations. Snapshot creation validates files, and import checks rule references before writing, so repeated invalid imports fail consistently.

The relevant package tests and `git diff --check` pass. This work item is complete.