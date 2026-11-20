Fixed `DeviceConfig` loading in [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts). Persisted fields now live in one config object; old credential arrays migrate to objects keyed by user ID and load into a Map. Initialization preserves the recognized fields and skips storage writes when the version and signup token are already current.

The source and test TypeScript checks pass. The client suite passed all 3,081 assertions on the final run.

The tests generated two untracked SQLite files. Automatic approval review rejected the cleanup command because it used `rm -f`, so I left those files in place.