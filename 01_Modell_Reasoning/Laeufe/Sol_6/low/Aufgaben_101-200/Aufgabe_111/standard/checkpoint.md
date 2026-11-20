Task: add Amazon Linux 2023+ version and EOL support.
Changed: config/os.go, config/os_test.go, scanner/redhatbase.go, oval/redhat.go.
Verification: go test ./config ./scanner ./oval passed.
