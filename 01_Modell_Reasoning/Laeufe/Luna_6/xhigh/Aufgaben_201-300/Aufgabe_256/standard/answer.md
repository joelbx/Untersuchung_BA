Updated [play.py](/app/lib/ansible/playbook/play.py:101): `Play.load` no longer derives or mutates `name`, `get_name` derives it from `hosts`, and `_validate_hosts` raises the requested parser errors when `hosts` is present but invalid. The existing integration assertion now expects the new empty-host message in [runme.sh](/app/test/integration/targets/playbook/runme.sh:38).

This checkout provides `is_sequence` in `ansible.module_utils.common.collections`; `ansible.utils.collection_loader` does not expose it.

**Verification:** 10 `Play` unit tests passed; the playbook integration target exited with code 0.