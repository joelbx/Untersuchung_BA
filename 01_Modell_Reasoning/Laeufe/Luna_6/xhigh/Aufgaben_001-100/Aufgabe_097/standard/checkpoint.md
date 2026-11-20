# Checkpoint

Task: Drop controller support for Python 3.10 and align collection tar extraction/install behavior with the issue requirements.

Implementation checkpoint: The controller minimum, ansible-test controller matrix, packaging metadata, controller-only compatibility cleanup, collection extraction behavior, and changelog fragment have been updated. Existing tests have been adjusted for direct TarFile member lookup.

Validation: `git diff --check` passes. The available interpreter is Python 3.11.13, so the existing unit tests ran with a narrowly scoped shim that bypassed only the 3.12 startup gate. Results: 239 passed; entry-point messages, package metadata, controller/remote version lists, and TOML loading were also checked. Both CLI entry points reject the available Python 3.11 interpreter with the same message.
