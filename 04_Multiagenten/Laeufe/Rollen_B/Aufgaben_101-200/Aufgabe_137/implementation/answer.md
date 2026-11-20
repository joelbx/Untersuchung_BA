Added tracing sampling and propagator configuration, defaults, validation, schema support, and runtime wiring. Added tests for loading, boundaries, supported values, and exact error messages.

Formatting, JSON parsing, and `git diff --check` pass. Go tests could not start offline because several existing dependencies are missing from the local module cache.