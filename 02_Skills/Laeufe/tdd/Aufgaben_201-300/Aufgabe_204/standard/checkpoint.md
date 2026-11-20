# Checkpoint

Task: Parse common text dates during contact import, preserve valid existing dates, and verify vCard serialization.

Implemented:
- Added `guessDateFromText` for ISO and native text formats, with validation against invalid calendar rollover.
- CSV birthday and anniversary conversion now use it; vCard property conversion returns existing valid dates or parsed text and leaves invalid dates unset.
- Added contact regression tests including CSV-to-vCard serialization.

TDD: The initial shared suite showed the new CSV date test failing and invalid vCard dates defaulting to today; direct checks reproduced the invalid slash-date rollover before its fix.

Verification:
- `yarn workspace @proton/shared check-types`: passed.
- `node_modules/.bin/eslint packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts packages/shared/test/contacts/csvFormat.spec.ts --quiet`: passed.
- Full shared Karma suite via local Chromium executable: 878 tests, 876 passed, 2 failed. Contact date tests all passed. The same two unrelated failures appeared in the prior run: `cookie helper > should expire cookies` (expected `name=125`, got empty string) and `toBase64 > should be an empty base64 on undefined file` (expected `data:`, got `data:application/octet-stream;base64,`). Command: `node -e "require('playwright').chromium.executablePath = () => '/usr/bin/chromium'; const {Server}=require('karma'); new Server({configFile:'/app/packages/shared/test/karma.conf.js',singleRun:true}, code => process.exit(code)).start();"`.
- Initial `yarn workspace @proton/shared test` could not launch its configured Playwright Chromium because `/root/.cache/ms-playwright/chromium-1045/chrome-linux/chrome` was absent. Used installed `/usr/bin/chromium` through the command above; no downloads or harness configuration changes.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `grep`/`find` for inspection.
