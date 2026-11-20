# Checkpoint

Task: Replace deprecated `:buffer` with `:tab-select` in command registration, completion, help, and configuration examples.

Completed: Renamed the command and tab completion providers (`tabs`, `other_tabs`), updated the default `gt` binding and current help, and migrated relevant unit, end-to-end, and manual tests. Added end-to-end cases for count precedence and URL matching. Historical changelog entries remain as historical records.

Verification: `git diff --check` clean. With manually managed Xvfb, 159 unit tests passed and 1 was expected to fail. With WebEngine, 13 tab-select end-to-end scenarios passed and 1 existing scenario was skipped; 2 completion end-to-end scenarios passed. The command registry contains `tab-select` and excludes `buffer`.
