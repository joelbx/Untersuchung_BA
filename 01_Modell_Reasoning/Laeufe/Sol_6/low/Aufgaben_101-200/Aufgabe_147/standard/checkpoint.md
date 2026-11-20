Task: Fix DeviceConfig load/migration overwrite.
Status: Complete. DeviceConfig now uses one config object, exact underscored persisted keys, keyed credentials migration, and conditional initialization writes. Updated tests for keyed migration and no-write reload. Verified with npx tsc --noEmit and npm run testclient (3054 assertions passed).
