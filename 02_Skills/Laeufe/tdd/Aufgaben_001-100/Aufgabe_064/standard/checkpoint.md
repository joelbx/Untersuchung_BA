# Checkpoint

Task: simplify `useMyCountry` to return country or undefined, migrate named consumers, and adjust PhoneInput default-country adoption.

Workflow: assigned test-driven-development skill; add a failing behavior test before production edits, then run focused and project tests. External research and downloads are prohibited.

Initial state: git status clean. `rg` is unavailable (`/bin/bash: rg: command not found`); use local `grep`/`find`.

Verification:
- `yarn workspace @proton/components test --runInBand --watch=false components/v2/phone/PhoneInput.test.tsx hooks/useMyCountry.test.ts`: passed (18 tests).
- `yarn workspace @proton/components test --runInBand --watch=false`: passed (155 suites, 1108 tests; 2 suites skipped).
- `yarn workspace @proton/components check-types`: failed at unchanged `packages/crypto/lib/worker/api.ts:579:77`, TS2345. The installed root `openpgp` PartialConfig is incompatible with `pmcrypto/node_modules/openpgp` PartialConfig (preferredHashAlgorithm/hash.md5). Type checking is therefore not fully verified; no reported diagnostic points to edited files.
- `yarn workspace proton-account check-types`: failed at unchanged `packages/crypto/lib/worker/api.ts:579:77`, same TS2345 root versus nested `openpgp` type conflict. No reported diagnostic points to edited files.
- `yarn workspace proton-mail check-types`: failed at unchanged `packages/crypto/lib/worker/api.ts:579:77`, same TS2345 root versus nested `openpgp` type conflict. No reported diagnostic points to edited files.
