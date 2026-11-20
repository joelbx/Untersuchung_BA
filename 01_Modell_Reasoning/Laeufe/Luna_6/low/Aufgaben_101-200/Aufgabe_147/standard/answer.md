Implemented the `DeviceConfig` persistence changes in [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts).

Configuration now lives in one object with the required underscored keys. Loading migrates legacy credentials into a user ID keyed object, restores them to a `Map`, and writes only after migration or signup token generation. Invalid JSON and unavailable storage fall back to defaults. The class also exposes `Version` and `LocalStorageKey`, and accepts explicit version and storage constructor parameters.

`npm run types` passed. The DeviceConfig test runner started building the client tests, but did not report a test result.