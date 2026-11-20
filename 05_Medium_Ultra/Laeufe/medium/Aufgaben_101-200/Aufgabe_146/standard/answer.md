Added `/proc/sysinfo` hardware facts for IBM Z. When the file exists, `get_sysinfo_facts()` returns the five requested keys, reads Manufacturer, Type, and Sequence Code, and removes leading zeros from the serial. When the file is absent, it returns `{}`. The values now flow into `gather_facts`.

The relevant tests passed: **108 passed, 5 skipped**.