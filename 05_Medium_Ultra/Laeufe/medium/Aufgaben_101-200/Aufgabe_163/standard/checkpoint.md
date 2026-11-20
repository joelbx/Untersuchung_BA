Goal: Support discrete database configuration with URL precedence, protocol validation, safe errors, and consistent migration settings.
Completed: Added DatabaseProtocol and discrete db fields; default ports and driver URLs; explicit field-qualified validation; URL precedence in loading and resolution; shared connection setup for Open and NewMigrator (configuration by value); redacted URL parsing and connection-open errors; qualified TLS certificate errors; documented fields and added relevant tests.
Verification: go test ./config ./storage/db ./cmd/flipt passed; git diff --check passed.
