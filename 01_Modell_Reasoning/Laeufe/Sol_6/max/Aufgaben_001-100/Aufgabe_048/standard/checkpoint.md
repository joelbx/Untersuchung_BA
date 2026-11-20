# Plugin resolution issue checkpoint

- Started: inspect plugin loader, plugin exceptions, display, template, action, and task executor paths.
- Repository baseline: clean working tree.
- Implemented contextual plugin exceptions, `get_with_context`, tombstone errors, centralized display formatting, and action/connection/Jinja consumers.
- Verified: 148 focused unit tests pass; `git diff --check` passes.
- Broader combined run: 462/472 passed. Collection import and display singleton failures depend on suite order; the collection loader file passes in its own process (56 tests), and the display warning case passes by itself. The facts FQCN case still fails when its test file runs in its own process on a configuration lookup path that this change does not touch.
- Ready for coordinator export of checked-out file changes.
