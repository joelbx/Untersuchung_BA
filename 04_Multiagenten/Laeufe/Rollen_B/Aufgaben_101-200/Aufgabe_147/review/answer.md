VERDICT: FIX

**Code defect:** The patched loader reads only `_themeId`. The previous loader also accepted legacy `_theme`, so migrating a stored config that has only `_theme` resets the selected theme to `light` and writes that value. Copy `_theme` to `_themeId` during migration when `_themeId` is absent. See [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts:118).

An array of `_credentials` with a missing or nonnumeric `_version` is also loaded as an empty Map. Migration should recognize the array shape before rewriting storage. See [DeviceConfig.ts](/app/src/misc/DeviceConfig.ts:106).

**Tests:** `npm run testclient` passed (3,071 assertions); `npm run types` passed. The existing tests do not cover these migration cases. **TEST_ENVIRONMENT_PROBLEM:** None.