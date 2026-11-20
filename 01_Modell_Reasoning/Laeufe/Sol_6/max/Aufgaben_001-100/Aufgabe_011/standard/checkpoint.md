# Issue checkpoint

- Goal: fix unset handling, module errors and deprecations, lookup messages, YAML legacy constructors, templar overrides, timedout, and early CLI errors.
- Initial state: clean working tree; no AGENTS.md found.
- Plan: locate implementations and existing tests, make focused edits, run relevant local tests, and record results here.
- Findings: module deprecations pass through task result compatibility and callback `_deprecated`, bypassing the ordinary `Display.deprecated` check; templar merges `None` directly into validated overrides; lookup warn/ignore currently use inconsistent messages.
- Implementation choice: use one private `_UNSET` object from `module_utils._internal` for internal option state, and filter module deprecations in their task context before callbacks receive them.
- Completed: fixed module parameter and exception handling, YAML legacy constructors, `None` templar overrides, lookup warn/ignore messages, early CLI errors, deprecation filtering and disable hint, and Boolean `timedout` behavior. Replaced Ellipsis as an internal option sentinel across affected code paths.
- Verification: 475 passed, 1 skipped across 18 relevant unit-test files; `git diff --check` clean. Target-side deprecation tests now explicitly use target-side mode because controller imports activate controller warning behavior during pytest collection.
