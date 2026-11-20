# Checkpoint

- Completed: controller minimum raised to Python 3.12 in CLI, ansible-test entry point, package metadata, and controller test matrix.
- Completed: removed the collection TarFile private cache and changed directory extraction to use `tar.getmember(dirname)` unchanged, with the specified AnsibleError message.
- Completed: simplified obsolete controller compatibility branches and comments, updated requirements/constraints, and added a public changelog fragment.
- Verification: 74 targeted tests passed, 1 skipped; compileall and `git diff --check` passed. Both entry points emit the same minimum-version error under installed Python 3.11.
- Limitation: role/CLI tests cannot collect on installed Python 3.11 because the new 3.12 gate rejects it; no Python 3.12 interpreter is installed.
