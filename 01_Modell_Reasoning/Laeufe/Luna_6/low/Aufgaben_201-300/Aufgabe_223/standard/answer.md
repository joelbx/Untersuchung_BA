Implemented shebang extraction and resolution for Python module data. Module interpreters and arguments are preserved unless an interpreter override applies, and the encoding declaration is inserted immediately after an existing shebang. Added unit coverage for interpreter parsing and shebang preservation.

Verification: **41 focused tests passed**; `git diff --check` passed.