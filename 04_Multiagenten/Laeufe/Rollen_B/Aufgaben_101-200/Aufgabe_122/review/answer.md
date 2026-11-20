VERDICT: FIX

**Code defects:** None confirmed in the reviewed patch. The storage validation, readonly selector, header badge and icons, and authentication bootstrap match the requested behavior. The required [invalid_readonly.yml](/app/internal/config/testdata/storage/invalid_readonly.yml) exists.

**Tests:** `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/cmd` passed both packages. `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** In `/app/ui`, `npm test -- --runInBand --watch=false` and `npm run build` both exited 127 because `npm` is unavailable. Provide Node.js, npm, and the project’s existing dependencies, then rerun those commands before accepting the patch.