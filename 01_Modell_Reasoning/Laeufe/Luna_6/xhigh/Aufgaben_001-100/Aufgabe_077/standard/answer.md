Implemented date based deprecations across Python modules, C# modules, Display, and validate-modules. This adds `removed_at_date`, date support for deprecated aliases, `YYYY-MM-DD` output, validation for alias entries, and date aware display messages.

The focused Python suites passed: **96 passed**. The `exit_json()` merge and formatting smoke check, Python compile checks, and `git diff --check` also passed.

I couldn’t run the validate-modules schema at runtime because Voluptuous is unavailable, or the Windows integration suite in this Linux environment.

Key changes: [basic.py](/app/lib/ansible/module_utils/basic.py:726), [warnings.py](/app/lib/ansible/module_utils/common/warnings.py:23), [Ansible.Basic.cs](/app/lib/ansible/module_utils/csharp/Ansible.Basic.cs:245), and [display.py](/app/lib/ansible/utils/display.py:252).