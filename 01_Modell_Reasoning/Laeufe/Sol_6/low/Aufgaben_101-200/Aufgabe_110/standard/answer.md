Added the download mechanism outcome metric to the existing metrics infrastructure. Terminal outcomes now include status, retry, and the selected mechanism; stateful downloads use `meta.size`, and preview downloads pass their size through the report call. The new schema restricts the labels to the requested values.

The relevant hook tests pass (16/16), and `git diff --check` passes.