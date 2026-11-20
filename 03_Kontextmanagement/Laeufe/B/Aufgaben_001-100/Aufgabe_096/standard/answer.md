Fixed the `atomic_move()` permission issue. New files use a `0600` default, and modules that accept `mode` warn when it was omitted. Setting a mode clears the warning for that path.

The focused tests passed (**46/46**), and `git diff --check` passed.