Updated the config loader to read the three database pool options and `meta.check_for_updates`. The omitted update-check value is now false; the default and deprecated fixtures still load field-for-field as `Default()`. Added regression coverage for explicit pool values, explicit update-check values, and omitted values.

The config, startup, and database package tests passed.