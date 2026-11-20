# Checkpoint

Task: update OS end-of-life data and Windows KB rollup mappings per the issue.

Initial inspection: repository root is `/app`; no `AGENTS.md` files were found in the parent tree. `rg` is unavailable in this environment, so use `find` and standard shell tools for repository inspection.

Next: inspect existing lifecycle data, Windows mappings, and their tests; preserve prior mappings and chronological revisions; update existing code and run the relevant existing tests.

Progress: updated Fedora 37/38/40, SUSE Enterprise Desktop/Server versions 13/14, and macOS 11/15 entries. Extended Windows 10 22H2, Windows 11 22H2 and 23H2 (22631), and Server 2022 rollup tables with the requested KBs and named revision/KB fields. Updated existing lifecycle and kernel-version test expectations for these mappings.

Verification: `gofmt` and `git diff --check` completed. `go test ./config ./scanner` is running; initial build is compiling the repository's large dependency graph.

Completed verification: `go test ./config ./scanner` passes after the updates; `gofmt` and `git diff --check` pass. The existing detector tests now cover newly listed KBs as unapplied on older revisions and applied on the synthetic high Server 2022 revision.
