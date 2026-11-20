# Checkpoint

Task: Replace deprecated `:buffer` with `:tab-select` throughout command registration, tab completion, help, and configuration examples.

Completed: registered `tab_select` in place of `buffer`; renamed tab completion providers to `tabs` and `other_tabs`; updated the default `gt` binding, generated command/settings help, manual example, and affected test scenarios. Added browser scenarios for URL matching and count precedence.

Verification: 185 unit tests passed, 1 expected failure; 15 tab selection/completion browser scenarios passed, 1 existing skip; 2 related browser scenarios passed. Direct registration and completion-list smoke check passed. The browser suite used QtWebEngine because QtWebKit is unavailable in this environment.

Final review: `git diff --check` passed. No deprecated command references remain in current code, help, settings, or test examples. Historical changelog entries retain the command name used in past releases.
