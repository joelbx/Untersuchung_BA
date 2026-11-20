# Fault localization checkpoint

- Scope: diagnosis only; no project source or tests changed.
- `LinuxHardware.populate()` in `lib/ansible/module_utils/facts/hardware/linux.py` calls `get_dmi_facts()` and merges its result, but never reads `/proc/sysinfo`.
- `get_dmi_facts()` reads `/sys/devices/virtual/dmi/id/*` or `dmidecode`, filling unavailable fields with `NA`; this explains the s390 result.
- Likely fix: add `LinuxHardware.get_sysinfo_facts()` and merge its returned values in `populate()` after DMI facts so available s390 fields replace `NA`.
- Contract: absent `/proc/sysinfo` gives `{}`; present file gives exactly `system_vendor`, `product_name`, `product_serial`, `product_version`, `product_uuid`, initialized to `NA`; parse `Manufacturer:`, `Type:`, and `Sequence Code:`; strip leading zeroes from serial. `product_version` and `product_uuid` remain `NA` absent a specified source.
- Existing hardware unit tests cover mounts, block devices, and s390 CPU data, but no sysinfo/DMI behavior was found.
