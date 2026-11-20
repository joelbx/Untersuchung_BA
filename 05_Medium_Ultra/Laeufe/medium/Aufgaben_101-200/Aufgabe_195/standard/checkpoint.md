Task: separate configuration warnings from Config through Result and deprecate ui.enabled.
Status: implemented and verified.
Changes: Load returns Result; deprecation detection uses keys present in the config file before defaults; caller logs Result.Warnings during command initialization; existing tests updated for separate warnings and explicit false keys.
Verification: GOPROXY=off go test ./internal/config ./cmd/flipt (passed); git diff --check (passed).
