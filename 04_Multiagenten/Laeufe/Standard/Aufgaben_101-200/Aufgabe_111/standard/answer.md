Amazon Linux 2023 detection now preserves its version through scanning and OVAL lookup, uses ALAS2023 advisory links, and skips the unnecessary `yum-utils` dependency. I also added version and EOL mappings for 2023, 2025, 2027, and 2029, with tests for support end dates and unknown releases.

The relevant `config`, `oval`, `scanner`, and `models` tests pass offline.