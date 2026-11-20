Task: Implement s390 hardware facts from /proc/sysinfo in LinuxHardware.

Requirements: Return {} if /proc/sysinfo is unavailable; otherwise return exactly system_vendor, product_name, product_serial, product_version, and product_uuid, defaulting each to "NA". Parse Manufacturer:, Type:, and Sequence Code: lines and remove leading zeros from the serial.

Progress: Inspecting existing implementation and focused tests before editing.
