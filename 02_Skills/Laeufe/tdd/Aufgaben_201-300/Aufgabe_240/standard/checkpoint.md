Task: Add netapp_e_drive_firmware Ansible module.
Implemented module and focused unit tests with test-first red/green cycles. Initial red: module missing; second red: upload URL incorrectly included storage-system prefix. Both resolved.
Checks:
- `PYTHONPATH=lib:test python -m pytest -q test/units/modules/storage/netapp/test_netapp_e_drive_firmware.py`: 6 passed.
- `python -m py_compile lib/ansible/modules/storage/netapp/netapp_e_drive_firmware.py`: passed.
- `git diff --check`: passed.
- `PYTHONPATH=lib:test python -m pytest -q --tb=short --disable-warnings test/units/modules/storage/netapp`: exit 1; 126 passed, 590 skipped, 3 collection errors. Existing test_netapp_e_iscsi_interface.py, test_netapp_e_iscsi_target.py, test_netapp_e_mgmt_interface.py require unavailable `mock` package (`ModuleNotFoundError: No module named 'mock'`). No download requested.
- `PYTHONPATH=lib:test python -m pytest -q --tb=line --disable-warnings`: failed in collection with `SystemExit: 1` from test/integration/targets/async/library/async_test.py; fixture instantiates AnsibleModule without parameters.
- `PYTHONPATH=lib:test python -m pytest -q --tb=short --disable-warnings test/units`: exit 1; 226 failed, 6145 passed, 813 skipped, 541 errors; broad pre-existing environment/dependency problems. Output in /tmp/netapp-drive-all-units.log.
Uncertainty: no local drive firmware API response fixture exists. Compatibility parsing and payload shape follow the issue's documented keys and local NetApp request conventions; live controller behavior was not verified.
