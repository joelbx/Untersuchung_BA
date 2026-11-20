# Checkpoint

Task: Repair contact import date parsing and preserve calendar values through vCard serialization.

Status: Implemented shared `guessDateFromText` parser using `parseISO` followed by JavaScript date parsing, wired it into CSV and vCard helpers, and removed the vCard helper's default-to-today behavior for unparseable values. Added parsing and CSV-to-vCard serialization coverage in `packages/shared/test/contacts/property.spec.ts`.

Checks:
- `../../node_modules/.bin/tsc --noEmit --pretty false` in `packages/shared`: passed.
- `../../node_modules/.bin/eslint lib/contacts/property.ts lib/contacts/helpers/csvFormat.ts test/contacts/property.spec.ts --quiet` in `packages/shared`: passed.
- `git diff --check`: passed.
- `../../node_modules/.bin/karma start test/karma.conf.js --single-run` in `packages/shared`: first attempt could not launch ChromeHeadless because `/root/.cache/ms-playwright/chromium-1045/chrome-linux/chrome` was missing. A temporary symlink to the installed `/usr/bin/chromium` allowed the second attempt to run; the symlink was removed afterward. The contact parsing and serialization tests passed, but the full suite exited 1: 876 passed, 2 failed. Unrelated failures were `toBase64 / should be an empty base64 on undefined file` (expected `data:`, received `data:application/octet-stream;base64,`) and `cookie helper / should expire cookies` (expected `name=125`, received empty string). These appear browser-environment-dependent; the full suite remains failing.
- `rg` was unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.

After making the serialization assertions explicit, reran `../../node_modules/.bin/karma start test/karma.conf.js --single-run` in `packages/shared` with the same temporary Chromium symlink, then removed it. All new contact tests passed. Full suite again: 878 executed, 876 passed, same two unrelated browser-dependent failures (`cookie helper / should expire cookies` and `toBase64 / should be an empty base64 on undefined file`). `git diff --check` passed after the final edit.
