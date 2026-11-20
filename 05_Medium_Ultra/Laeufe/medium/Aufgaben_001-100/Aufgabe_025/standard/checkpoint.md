Task: Support direct ${VARIABLE_NAME} substitution in YAML configuration values.
Status: Complete. Added a first-position decode hook for exact environment references and loader/edge-case tests. Full internal/config package tests pass with GOWORK=off, GOPROXY=off, GOTOOLCHAIN=local, and -mod=readonly; git diff --check passes.
