Fixed both reviewed defects in [module_common.py](/app/lib/ansible/executor/module_common.py): legacy redirects now use the full dotted name below `ansible.module_utils`, and a missing redirect target collection raises an `AnsibleError` naming that collection. Added regression tests.

The exact test command from the review passed: **51 passed**. `git diff --check` also passed.