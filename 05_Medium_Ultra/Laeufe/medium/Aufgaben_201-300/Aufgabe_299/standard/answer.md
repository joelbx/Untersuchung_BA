Added filesystem completion to `:open`. The new `Filesystem` category follows `completion.open_categories` order and suggests favorite paths, absolute paths, local `file:///` URLs, and `~` paths. Both settings are documented in the help.

Verification: 101 completion and config tests passed; `git diff --check` passed. Pytest exited with an X11 teardown error after reporting the passing tests.