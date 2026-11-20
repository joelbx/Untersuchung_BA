# Checkpoint

Task: implement explicit storage read-only configuration, validation and metadata propagation, frontend configuration selection/state, storage indicators in the header, and authentication bootstrap behavior; add the requested invalid configuration fixture.

Constraints: use repository code and existing tests only; preserve git history, index baseline, and harness configuration.

Status: implemented backend read-only configuration and non-database validation, metadata propagation through the existing config serialization, frontend config selector and read-only fallback, storage icons in the header, the requested invalid configuration fixture, and authentication bootstrap bypass for all non-database storage types when authentication is disabled.

Verification: `go test ./internal/config ./internal/cmd` passed. UI test/build could not run because `npm` is unavailable in the environment. `git diff --check` passed.
