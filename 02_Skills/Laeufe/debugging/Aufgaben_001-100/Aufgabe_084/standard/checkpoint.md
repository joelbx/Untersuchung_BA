# Checkpoint

Task: add recursive removeTechnicalFields(entity) to EntityUtils.
Status: investigating repository behavior and existing tests.

Root cause: InstanceMapper attaches encrypted restore metadata and errors to decrypted entities and nested aggregates. A clone copies those enumerable properties; EntityUtils has no recursive cleanup API. The mapper reads the metadata during update encryption, so removal is appropriate only for new instances.
Pattern: metadata keys use the three requested prefixes; aggregates are nested objects or arrays. Other entity fields must retain their references.
Hypothesis: recursively visiting own enumerable object properties and deleting keys with the three prefixes will clean roots and aggregates while preserving all unrelated fields.
Regression before fix: `./node_modules/.bin/tsc --noEmit --incremental false -p test/tsconfig.json` exited 2 with missing removeTechnicalFields export (plus test assertion type errors, corrected in test source before implementation).

Implementation: added public generic void removeTechnicalFields to EntityUtils. It deletes matching own enumerable keys recursively in objects and arrays, preserves other properties, and tracks visited objects to handle shared or cyclic references.
Verification: `./node_modules/.bin/tsc --noEmit --incremental false -p test/tsconfig.json` exited 0; `npm run test:app -- -f` exited 0 with 8,681 assertions passed; targeted Prettier and ESLint exited 0; `git diff --check` exited 0.
