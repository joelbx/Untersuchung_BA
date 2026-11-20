Implemented the non-destructive config load and migration in [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts:48). Current configs with a signup token load without a storage write; migrations and token generation persist only the recognized underscored keys. Credentials are held in a `Map`, serialized by user ID, and updates retain an existing database key.

Updated [DeviceConfigTest.ts](/app/test/client/misc/DeviceConfigTest.ts:96) to cover migration, no-write loads, idempotence, token generation, and recovery.

Verification: `npm run types` passed; `npm run testclient` passed all 3,074 assertions. The runner logged a non-blocking `better-sqlite3` package warning.