Correction round started: inspecting current patch and reviewer finding on RPM owner identity.
Found defect: parseOwnerPkgs accepts owner by name alone. Will require matching version, release, and architecture and cover mismatched owners in tests.
Fixed owner association: RPM owner must match stored package version, release, and architecture. Added mismatch regression cases. GOPROXY=off GOSUMDB=off go test ./scan passed; git diff --check passed.
