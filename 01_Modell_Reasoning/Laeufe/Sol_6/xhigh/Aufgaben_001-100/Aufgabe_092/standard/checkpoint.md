# Checkpoint

Task: collection install --upgrade implementation.
Implemented: CLI -U/--upgrade forwarding; upgrade-aware dependency resolver; installed-dependency validation with --no-deps; version-based idempotency; opt-in prereleases; integration upgrade.yml; unit and changelog coverage.
Validation: 267 galaxy and CLI unit tests passed after functional changes; final focused 148 tests passed; YAML parsed; git diff --check clean.
Integration upgrade.yml requires local Galaxy services and was not executed here.
