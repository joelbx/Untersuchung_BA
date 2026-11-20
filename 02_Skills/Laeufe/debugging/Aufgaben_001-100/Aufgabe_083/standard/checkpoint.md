# XAttr refactor checkpoint

Started investigation. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep` instead. No code changes yet.

Investigation: implementation is `applications/drive/src/app/store/_links/extendedAttributes.ts` (the issue's services path does not exist). The factory pushes a zero remainder for exact chunk multiples. The parser dereferences `Media.Width` and `Digests.SHA1` when those values can be JSON null. `any` masks this. One production encryption call site exists in upload worker. The encryption function must retain two key parameters; interpret "sole parameter" as sole metadata parameter per the detailed interface.

Hypothesis: a typed object parameter, conditional remainder, and guarded parsed object fields fix the observed failures while preserving serialization for valid inputs.

Red tests before patch: from `/app/applications/drive`, `../../node_modules/.bin/jest src/app/store/_links/extendedAttributes.test.ts --runInBand --coverage=false` failed with `RangeError: Invalid array length` for object input and `TypeError: Cannot read properties of null (reading 'SHA1')` for malformed JSON. Root causes confirmed: positional factory contract and missing null checks.

Patch: object metadata argument for creation/encryption; upload worker updated. Added recursive DeepPartial, exported XAttr types, immutable created fields, conditional final block and digest omission, typed parser input with null-safe extraction. A service-path re-export provides the specified public location while preserving the existing store implementation and imports.

Checks: focused Jest suite passed (5 tests); Drive `tsc --noEmit --incremental false -p tsconfig.json` passed before the final service re-export and digest shape adjustment. Prettier check passed. Final type check pending.

Tooling note: initial Jest command from `/app` failed because it used the root Jest config, producing duplicate mock warnings and a TypeScript parse error. Running from `applications/drive` used the project's config and executed the tests.

Final checks: focused Jest suite passed (5/5); full Drive `tsc --noEmit --incremental false -p tsconfig.json` exited 0; targeted ESLint exited 0 after adjusting `DeepPartial` array notation; targeted Prettier check exited 0 before that notation adjustment, which follows its same formatting convention; `git diff --check` exited 0. No dependencies downloaded.
