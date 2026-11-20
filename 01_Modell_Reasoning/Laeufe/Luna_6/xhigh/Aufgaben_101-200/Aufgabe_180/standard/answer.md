Implemented the lifecycle updates in [config/os.go](/app/config/os.go:236) and extended Windows 10, Windows 11, and Server 2022 rollup mappings in [scanner/windows.go](/app/scanner/windows.go:2812). Added tests for the updated EOL dates and KB classification below and above mapped revisions.

`go test ./config ./scanner` and `git diff --check` pass.