Task: add HTTPS support in /app.
Current findings: configuration is in cmd/flipt/config.go; startup listeners are in cmd/flipt/main.go. Existing loader uses global Viper and no argument. Server currently exposes HTTP and insecure gRPC only.
Plan: add Scheme and TLS settings with validation, update loader and call sites, serve HTTPS and TLS gRPC, update sample configuration/docs, run local Go tests.
Implemented: path-based isolated Viper loader, Scheme/defaults/validation, HTTPS REST/UI and TLS gRPC with trusted gateway connection, docs and config examples. Added focused configuration/handler tests. Go suite passed; local HTTPS and gRPC TLS smoke check passed, and REST gateway ListFlags returned 200 after startup.
