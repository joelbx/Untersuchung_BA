Task: support separate database credential keys while preserving URL precedence.
Status: implemented and verified.
Changes: added DatabaseProtocol and discrete database fields with validation; config loading chooses URL or fields; database connection derives engine-specific targets and applies pool settings; migration accepts application config by value and uses same connection path; errors distinguish parsing, validation, and connection failures and redact passwords; documented fields and added focused tests.
Verification: go test ./... passed; git diff --check passed. Existing sqlite3 C compiler warning remains in test output.
