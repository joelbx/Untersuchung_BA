Issue: config.Load omitted database pool options and meta.check_for_updates.
Implemented: databaseConfig has MaxIdleConn, MaxOpenConn, ConnMaxLifetime; Load reads their db keys and meta.check_for_updates only when set. Default() has CheckForUpdates false, matching the required absent-key value and default/deprecated fixture equality. Advanced fixture and TestLoad expectation cover nonzero pool options and an explicit true update flag.
Validation: go test ./config passed; go test ./... passed; git diff --check passed.
