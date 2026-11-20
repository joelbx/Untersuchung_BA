Task: align OS EOL data and Windows KB mappings, then run relevant existing Go tests.
Status: completed source and test changes in config/os.go, config/os_test.go, scanner/windows.go, and scanner/windows_test.go.
Verification: GOPROXY=off GOSUMDB=off go test ./config ./scanner passed; git diff --check passed.
