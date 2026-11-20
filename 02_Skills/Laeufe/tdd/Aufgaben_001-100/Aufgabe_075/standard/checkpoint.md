Task: add contextual user properties repository and migrate LastFM session storage.
Status: implemented. New user_props table, scoped repository, datastore method, LastFM switch, legacy session-key migration, and tests.
TDD: persistence isolation test failed first (undefined constructor), then passed; LastFM scrobbling test failed with data not found before switch, then passed; migration test failed with no rows before copy, then passed.
Verification: go test ./... passed. git diff --check passed. Compiler emitted existing sqlite3 and TagLib C/C++ warnings.
Tooling: rg unavailable (/bin/bash: rg: command not found); used grep/find.
