Added [netapp_e_drive_firmware.py](/app/lib/ansible/modules/storage/netapp/netapp_e_drive_firmware.py) with firmware upload, compatible drive selection, check mode, online or offline upgrades, optional waiting, and upgrade status reporting. Added [unit tests](/app/test/units/modules/storage/netapp/test_netapp_e_drive_firmware.py).

Validation: 13 new tests pass; the available NetApp suite reports 133 passed and 590 skipped. Three existing test files could not be collected because `mock` is unavailable. Documentation parsing and Python compilation pass.

Check mode evaluates firmware already staged on the controller; it does not upload files.