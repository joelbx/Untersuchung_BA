Implemented the `safe_eval` deprecation in [validation.py](/app/lib/ansible/module_utils/common/validation.py) and documented the delegating [AnsibleModule wrapper](/app/lib/ansible/module_utils/basic.py:1204). Calls now record an Ansible runtime deprecation targeting 2.21.

`check_type_dict` now parses JSON, then restricted Python literals, then validated `key=value` pairs. It returns dictionaries and raises descriptive `TypeError` messages for invalid input. The [changelog fragment](/app/changelogs/fragments/safe-eval-deprecation.yml) covers both APIs.

I delegated the call-site audit, changelog, and test coverage, then integrated and verified the patch. **134 relevant tests passed**, and `git diff --check` passed.