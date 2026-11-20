# Contact date import checkpoint

Task: implement `guessDateFromText`, use it for CSV and vCard imports, preserve calendar values on vCard serialization, and verify relevant tests.

Status: inspecting repository. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Verification so far:
- `yarn workspace @proton/shared check-types`: exit 0.
- `yarn prettier --check packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts`: exit 0 after formatting.
- `./node_modules/.bin/eslint packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts --quiet`: exit 0.
- `yarn workspace @proton/shared test -- --single-run`: webpack compiled, then Karma failed to launch bundled Playwright Chromium (`Cannot start ChromeHeadless`, `Can not find the binary /root/.cache/ms-playwright/chromium-1045/chrome-linux/chrome`). The file exists but cannot execute because its ELF interpreter is absent.
- `node -e "process.argv = [process.execPath, 'karma', 'start', 'test/karma.conf.js']; require('playwright').chromium.executablePath = () => '/usr/bin/chromium'; require('karma/lib/cli').run()"` in `packages/shared`: browser ran 875 tests; 873 passed, 2 failed. Contact property/import/vCard tests passed. Unrelated failures: `toBase64 / should be an empty base64 on undefined file` (expected `data:`, got `data:application/octet-stream;base64,`) and `cookie helper / should expire cookies` (expected `name=125`, got empty string).

Final verification after the last edit:
- Focused Karma command using system Chromium and `client.args: ['--grep=property']`: exit 0, 27 passed, 851 skipped.
- `yarn workspace @proton/shared check-types`: exit 0.
- `./node_modules/.bin/eslint packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts --quiet`: exit 0.
- `yarn prettier --check packages/shared/lib/contacts/property.ts packages/shared/lib/contacts/helpers/csvFormat.ts packages/shared/test/contacts/property.spec.ts`: exit 0.
- Full suite remains at the earlier observed 873 passed, 2 unrelated failures; it was not rerun after the final test-only edit.
