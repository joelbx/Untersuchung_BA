Task: Resolve DeviceConfig overwrite-on-load.
Implemented: one config object with the exact underscored persisted fields; conditional initialization writes; credential array and indexed-key migration to userId-keyed objects; Map deserialization; default recovery and token generation; no-op setter guards; explicit version/storage global initialization.
Verification: `npx tsc --noEmit --pretty false` passed; `npx tsc --project test/tsconfig.json --noEmit --pretty false` passed; `git diff --check` passed. `npm run testclient` was attempted but its build server failed compiling existing better-sqlite3 (missing dependency file under node_modules/better-sqlite3/build), before tests ran.
Constraints: local code/tests only; git history, index, and harness configuration untouched.
