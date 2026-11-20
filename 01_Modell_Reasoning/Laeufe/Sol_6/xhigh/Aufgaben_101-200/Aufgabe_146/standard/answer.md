Added `/proc/sysinfo` hardware facts for s390 and wired them into `setup` fact collection. The parser returns the five requested keys when the file exists, removes leading zeros from the serial, and returns `{}` when the file is absent.

Added tests for parsing and fact collection. All 21 hardware fact tests pass.