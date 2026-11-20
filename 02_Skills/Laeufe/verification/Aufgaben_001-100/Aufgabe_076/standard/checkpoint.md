# Address parsing checkpoint

Task: normalize comma/semicolon address tokens and bracketed recipient emails.

Initial repository status: clean (`git status --short` returned no entries).
Search tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local file search instead.

Next: locate parser and tests, patch behavior, run relevant existing tests, and record results.

Patch: added `splitBySeparator` to shared recipient parsing; fixed the bare bracketed email name; used the splitter for completed pasted addresses in both autocomplete versions; added shared parser tests.

Checks so far:
- `../../node_modules/.bin/tsc --noEmit -p tsconfig.json` in `/app/packages/shared`: exit 0.
- `NODE_ENV=test ../../node_modules/.bin/karma start test/karma.conf.js --single-run` in `/app/packages/shared`: exit 1 after webpack compiled; launcher error: `Can not find the binary /root/.cache/ms-playwright/chromium-1041/chrome-linux/chrome`. Test results remain unknown from this attempt. `/usr/bin/chromium` exists; retrying with a temporary launcher wrapper.
- Initial Prettier check found formatting in the new spec; formatted it and will recheck.

Final verification:
- `NODE_ENV=test ../../node_modules/.bin/karma start /tmp/address-karma.conf.js --single-run --reporters dots` in `/app/packages/shared`, using a temporary wrapper to point Karma at `/usr/bin/chromium` and filter `--grep=address input parsing`: exit 0, 3 executed, 835 skipped, 0 failures.
- `NODE_ENV=test ../../node_modules/.bin/karma start /tmp/address-karma.conf.js --single-run` in `/app/packages/shared`, using the temporary wrapper without a test filter: exit 1, 838 executed, 836 success, 2 failures (`cookie helper / should expire cookies`: expected `name=125`, got empty string; `toBase64 / should be an empty base64 on undefined file`: expected `data:`, got `data:application/octet-stream;base64,`). These are outside the edited parser. Full-suite status is failing.
- `../../node_modules/.bin/tsc --noEmit -p tsconfig.json` in `/app/packages/components`: exit 0.
- `node_modules/.bin/prettier --check packages/shared/lib/mail/recipient.ts packages/shared/test/mail/recipient.spec.ts packages/components/components/addressesAutomplete/AddressesAutocomplete.tsx packages/components/components/v2/addressesAutomplete/AddressesAutocomplete.tsx` in `/app`: exit 0.
- `git diff --check` in `/app`: exit 0.
