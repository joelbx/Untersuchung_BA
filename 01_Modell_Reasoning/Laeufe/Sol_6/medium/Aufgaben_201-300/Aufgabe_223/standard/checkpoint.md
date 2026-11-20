Task: preserve module shebang interpreters and arguments in Ansible module packaging, while honoring configured overrides and defaulting only for missing shebangs.
Completed: added shebang interpreter extraction, resolved new-style Python wrappers from source shebangs, preserved original shebang text and quoted arguments when possible, and aligned old-style module rewriting with the resolved interpreter. Added focused regression tests.
Verification: 47 tests passed in test/units/executor/module_common/test_module_common.py and test_modify_module.py; git diff --check passed.
