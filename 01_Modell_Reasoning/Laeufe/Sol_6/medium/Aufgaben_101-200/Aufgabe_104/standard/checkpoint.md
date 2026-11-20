Task: Add metadata configuration with CheckForUpdates defaulting to true, compatible with JSON/YAML loading and validation.
Status: Complete. Added Config.Metadata.CheckForUpdates, default true, Viper loading from metadata.check_for_updates, example default YAML, and YAML/JSON loading tests. Updated existing expected config.
Verification: GOPROXY=off GOSUMDB=off go test ./config (pass); GOPROXY=off GOSUMDB=off go test ./cmd/flipt ./config (pass); git diff --check (pass).
