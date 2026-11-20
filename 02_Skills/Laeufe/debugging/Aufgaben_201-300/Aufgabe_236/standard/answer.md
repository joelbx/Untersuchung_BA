Updated [validation.py](/app/lib/ansible/module_utils/common/validation.py) so `check_type_dict` parses JSON, dictionary literals, and validated `key=value` pairs without calling `safe_eval`. Invalid inputs now raise `TypeError`.

Both `safe_eval` entry points are marked deprecated; calls through [AnsibleModule.safe_eval](/app/lib/ansible/module_utils/basic.py:1204) delegate to the global function and record the Ansible deprecation for version 2.21. I also added a [changelog fragment](/app/changelogs/fragments/safe_eval-deprecation.yml).

Verification: 168 relevant tests passed, and `git diff --check` passed.