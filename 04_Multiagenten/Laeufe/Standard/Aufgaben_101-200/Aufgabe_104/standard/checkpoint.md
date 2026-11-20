Task: add metadata configuration with CheckForUpdates defaulting to true, supported by JSON/YAML loading and validation.
Status: complete. Added Config.Metadata.CheckForUpdates, default true, Viper mapping for metadata.check_for_updates, default YAML documentation, and YAML/JSON loading coverage.
Verification: GOPROXY=off GOSUMDB=off go test ./config passed; GOPROXY=off GOSUMDB=off go test ./cmd/flipt ./config passed; git diff --check passed.
Constraints observed: used local repository and existing tests; did not change git history, index baseline, or harness configuration.
