Added [netapp_e_drive_firmware.py](/app/lib/ansible/modules/storage/netapp/netapp_e_drive_firmware.py) with firmware upload, drive selection, upgrade initiation, status polling, check mode, and the E-Series connection parameters.

The module compiles, and the 11 existing E-Series ASUP tests pass. Those tests do not exercise the new module’s controller API behavior.