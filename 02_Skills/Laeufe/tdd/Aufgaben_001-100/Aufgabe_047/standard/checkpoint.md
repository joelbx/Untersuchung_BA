# Hasher seeding issue

Status: implementation and regression tests complete. The hasher now accepts explicit per-ID seeds, reseeds with random seed strings, initializes missing IDs automatically, and hashes using the Hasher's maphash seed. Access to the seed map is synchronized.

RED verified: `GOTOOLCHAIN=local GOPROXY=off go test ./utils/hasher` fails to compile because `SetSeed` is missing on the hasher and package. This is the expected missing API under test.

GREEN verified: `GOTOOLCHAIN=local GOPROXY=off go test ./utils/hasher` passed. After refactoring, `GOTOOLCHAIN=local GOPROXY=off go test -race ./utils/hasher` passed. `git diff --check` passed.

Full suite: `GOTOOLCHAIN=local GOPROXY=off go test ./...` ran and failed only in `scanner/metadata/taglib` on `Correctly parses m4a (aac) gain tags` and `Correctly parses m4a (aac) gain tags (uppercase)`: each fixture returned duplicate `replaygain_album_gain` values `["0.37", "0.37"]` where the test expected a single `["0.37"]`. All other Go packages passed. These failures are outside the hasher path and were not changed here.

Tooling note: `rg --files -g 'AGENTS.md' -g '*hasher*' -g 'go.mod' -g 'Makefile' -g 'writing-good-tests.md'` failed because `rg` is not installed (`/bin/bash: rg: command not found`). I will use local `find` and `grep`.
